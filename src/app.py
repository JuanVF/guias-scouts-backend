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
from flask import Flask, send_from_directory
from controller.authentication import auth_blueprint
from controller.health import health_blueprint
from controller.user import user_blueprint
from controller.material import material_blueprint
from controller.progress import progress_blueprint
from controller.patrols import patrol_blueprint
from flasgger import Swagger
from flask_cors import CORS

app = Flask(__name__)

swagger = Swagger(app)
CORS(app)

# All routes
app.register_blueprint(auth_blueprint)
app.register_blueprint(health_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(material_blueprint)
app.register_blueprint(progress_blueprint)
app.register_blueprint(patrol_blueprint)


@app.route('/static/<filename>')
def download_file(filename):
    directory = app.static_folder  # Assuming file is in the static folder
    return send_from_directory(directory, filename, as_attachment=True, download_name=filename)


if __name__ == '__main__':
    app.run(debug=True)
