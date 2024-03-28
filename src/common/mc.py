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
from common.config import Config
import shutil
import subprocess
import re

config = Config()


class MCHandler:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.is_alias_set = False
            self.alias = config.MC_ALIAS
            self.secret_key = config.MC_SECRET_KEY
            self.access_key = config.MC_ACCESS_KEY
            self.minio_url = config.MINIO_URL
            self.bucket = config.MC_BUCKET
            self.mc_path = shutil.which('mc')

    def __execute(self, args) -> bool:
        if len(args) <= 0:
            return False

        to_execute = [self.mc_path] + args

        print(to_execute)

        result = subprocess.run(
            to_execute, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stderr)

        if result.returncode != 0:
            print(f"MCHandler-Error: Something wen't wrong {result.stderr}")

        return result.returncode == 0

    def __execute_with_output(self, args) -> bool:
        if len(args) <= 0:
            return False

        to_execute = [self.mc_path] + args

        result = subprocess.check_output(to_execute, shell=True, text=True)

        return result

    def get_signed_url(self, path):
        """Gets a file from MinIO using mc"""
        try:
            args = [
                "share", "download", f"{self.alias}/{self.bucket}/{path}"]

            output = self.__execute_with_output(args)

            urls = re.findall(r'https?://[^\s]+', output)

            if len(urls) < 1:
                raise Exception("File not found... error")

            return urls[1]
        except Exception as e:
            print(
                f"MC-Error: an error ocurred while getting the shared url for file '{path}'")

    def save_file(self, filename):
        """Gets a file from MinIO using mc"""
        try:
            args = [
                "cp", f"media/{filename}", f"{self.alias}/{self.bucket}/{filename}"]

            succeed = self.__execute(args)

            if not succeed:
                raise Exception("")
            return f"{self.minio_url}/{self.bucket}/{filename}"
        except Exception as e:
            print(
                f"MC-Error: an error ocurred while getting the saving the file '{filename}'")

    def connect(self):
        """Establishes the MinIO alias with mc"""
        try:
            print(f"MC: Setting alias {self.alias}")
            args = [
                "alias", "set", self.alias, self.minio_url, self.access_key, self.secret_key]

            succeed = self.__execute(args)

            if not succeed:
                raise Exception("")

            print(f"MC: Alias set {self.alias} successfully")

            self.is_alias_set = True

            print(f"MC: Creating bucket if not exists {self.bucket}")
            args = [
                "mb", f"{self.alias}/{self.bucket}", ]

            succeed = self.__execute(args)

            if not succeed:
                raise Exception("")

            print(f"MC: Bucket created {self.bucket} successfully")
        except Exception as e:
            print(
                f"MC-Error: an error ocurred while setting the alias '{self.alias}'")


mc_handler = MCHandler()
mc_handler.connect()
