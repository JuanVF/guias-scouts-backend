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
import hashlib
import jwt


def sha3_512_string(input_string):
    """
    Returns the SHA-3 512 bits in string format
    """
    # Convert the input string to bytes
    input_bytes = input_string.encode('utf-8')

    # Compute the SHA-3 hash with 512 bits output
    sha3_hash = hashlib.sha3_512(input_bytes).digest()

    # Convert the hash bytes to a hexadecimal string
    hash_string = sha3_hash.hex()

    return hash_string


def create_jwt(secret_key: str, payload) -> str:
    """
    Creates the JWT Token using the secret key and the payload
    """
    return jwt.encode(payload, secret_key, algorithm='HS256')
