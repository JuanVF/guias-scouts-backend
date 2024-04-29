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

from repository.progress import get_all_progress_types as repo_get_all_progress_types
from repository.progress import get_questions_by_progress_type_and_user_id as repo_get_questions_by_progress_type_and_user_id

def get_all_progress_types() -> list[dict]:
    """
    Service that can get all the progress types
    """
    progress_types = repo_get_all_progress_types()

    if len(progress_types) <= 0:
        return progress_types

    results = []

    for i in range(0, len(progress_types)):
        type = progress_types[i]

        results += [type.to_dict()]

    return results

def get_questions_by_progress_type_and_user_id(type: str, user_id : int) -> list[dict]:
    """
    Service that can filter questions by progress types and user id
    """
    questions = repo_get_questions_by_progress_type_and_user_id (type, user_id)

    if len(questions) <= 0:
        return questions

    results = []

    for i in range(0, len(questions)):
        question = questions[i]

        results += [question.to_dict()]

    return results