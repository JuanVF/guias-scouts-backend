# Copyright (c) 2024 Guias Scouts

# All rights reserved. This file and the source code it contains is
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
import os


class Config:
    def __init__(self):
        """Load environment variables."""
        self.DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
        self.DB_USERNAME = os.getenv('DB_USERNAME', 'root')
        self.DB_PASSWORD = os.getenv('DB_PASSWORD', 'tea')
        self.DB_DATABASE = os.getenv('DB_DATABASE', 'guias-scouts')
        self.MINIO_ENDPOINT = os.getenv(
            'MINIO_ENDPOINT', 'localhost:9000')
        self.MINIO_ACCESS_KEY = os.getenv(
            'MINIO_ACCESS_KEY', 'minioadmin')
        self.MINIO_SECRET_KEY = os.getenv(
            'MINIO_SECRET_KEY', 'minioadmin')
        self.SECRET_KEY_JWT = os.getenv('SECRET_KEY_JWT', 'wiuwiuwiu')
        self.SENDER_EMAIL = os.getenv('SENDER_EMAIL', 'tropa92cr@gmail.com')
        self.SENDER_EMAIL_PASSWORD = os.getenv('SENDER_EMAIL_PASSWORD', 'xteg jikb icmz ibup')


config = Config()
