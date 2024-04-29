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

import random
import string

generate_password = lambda length: ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?") for i in range(length))

def generate_confirmation_code():
    """
    Generate a unique confirmation code consisting of 3 uppercase letters followed by 3 random digits.
    """
    # Generar tres letras mayúsculas aleatorias
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))

    # Generar tres dígitos aleatorios
    numbers = ''.join(random.choices(string.digits, k=3))

    # Combinar las letras y los números para formar el código de confirmación
    confirmation_code = f"{letters}{numbers}"

    return confirmation_code
