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
FROM alpine:3.19.1

# Install all packages
RUN apk add --update python3 py3-pip curl

# Set the workdir
WORKDIR /app
COPY src/ /app
RUN mkdir /app/media/

# Set the virtual Environment
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Install all python dependencies
RUN pip install flask pydantic flasgger mysql-connector-python PyJWT flask-cors

# Create the user backend and grant permissions to run the project
RUN adduser -D backend
RUN chown -R backend:backend /app

USER backend

# Env Variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]