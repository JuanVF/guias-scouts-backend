# Copyright (c) 2024 Guias Scouts

# All rights reserved. This file and the media code it contains is
# confidential and proprietary to Guias Scouts. No part of this
# file may be reproduced, stored in a retrieval system, or transmitted
# in any form or by any means, electronic, mechanical, photocopying,
# recording, or otherwise, without the prior written permission of
# Guias Scouts.

# This file is provided "as is" with no warranties of any kind, express
# or implied, including but not limited to, any implied warranty of
# merchantability, fitness for a particular purpose, or non-infringement.
# In no event shall Guias Scouts be liable for any direct, indirect,
# incidental, special, exemplary, or consequential damages (including, but
# not limited to, procurement of substitute goods or services; loss of use,
# data, or profits; or business interruption) however caused and on any
# theory of liability, whether in contract, strict liability, or tort
# (including negligence or otherwise) arising in any way out of the use
# of this software, even if advised of the possibility of such damage.

# For licensing opportunities, please contact tropa92cr@gmail.com.
from common.db import connection


class ProgressTypes:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name
        }


class ProgressQuestion:
    def __init__(self, id, question, question_type_id, question_type, progress_type_id, progress_type, user_answer):
        self.id = id
        self.question = question
        self.question_type_id = question_type_id
        self.question_type = question_type
        self.progress_type_id = progress_type_id
        self.progress_type = progress_type
        self.user_answer = user_answer

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "question": self.question,
            "question_type": self.question_type,
            "question_type_id": self.question_type_id,
            "progress_type": self.progress_type,
            "progress_type_id": self.progress_type_id,
            "user_answer": self.user_answer,
        }


def get_all_progress_types():
    """
    Query all the progress types
    """
    try:
        result = []
        params = ()
        data = connection.execute_read_query("""SELECT 
                id, name
            FROM 
                `guias-scouts`.t_progress_type_table;""", params)

        if data and len(data) > 0:
            for i in range(0, len(data)):
                result += [ProgressTypes(*data[i])]

        return result
    except:
        return []


def get_questions_by_progress_type_and_user_id(type: str, user_id: int):
    """
    Filter questions by the progress type
    """
    try:
        result = []
        params = (user_id, type, )
        data = connection.execute_read_query("""SELECT 
                    pq.id,
                    pq.question,
                    qt.id AS question_id,
                    qt.name AS question_type,
                    pt.id AS progress_id,
                    pt.name AS progress_type,
                    COALESCE(pp.user_id IS NOT NULL, FALSE) AS user_answer
                FROM `guias-scouts`.t_progress_questions_table pq
                INNER JOIN `guias-scouts`.t_question_type_table qt ON pq.id_question_type = qt.id
                INNER JOIN `guias-scouts`.t_progress_type_table pt ON pq.id_progress_type = pt.id
                LEFT JOIN `guias-scouts`.t_protagonist_progress_table pp ON pq.id = pp.question_id AND pp.user_id = %s
                WHERE pt.name = %s;""", params)

        if data and len(data) > 0:
            for i in range(0, len(data)):
                result += [ProgressQuestion(*data[i])]

        return result
    except:
        return []


def insert_user_answers(user_id: int, answered_questions: list[ProgressQuestion]):
    """
    Insert user answers into the database
    """
    try:
        for question in answered_questions:
            if question.user_answer == 1:
                params = (question.id, user_id)
                connection.execute_query("""INSERT INTO 
                        `guias-scouts`.t_protagonist_progress_table (question_id, user_id)
                    VALUES 
                        (%s, %s);""", params)
            else:
                connection.execute_query("""DELETE FROM 
                        `guias-scouts`.t_protagonist_progress_table 
                    WHERE 
                        question_id = %s AND user_id = %s;""", (question.id, user_id))

        return True
    except Exception as e:
        print("Error inserting user answers:", e)

        return False
