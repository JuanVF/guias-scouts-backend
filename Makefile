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

build:
	docker build . -t guias-scouts-backend:$(TAG)

build_db:
	docker build -f Dockerfile.db -t guias-scouts-db:$(TAG) .

run_dev:
	export FLASK_APP=src/app.py
	cd src && python3 -m flask run

start_dev_env:
	docker-compose -f ./docker-compose.dev.yaml up -d

destroy_dev_env:
	docker-compose -f ./docker-compose.dev.yaml down

new_migration:
	@file_path="./migrations/$$(date "+%Y%m%d%H%M")-$(NAME).sql"; \
	touch $$file_path; \
	echo "-- Copyright (c) 2024 Guias Scouts" >> $$file_path; \
	echo "--" >> $$file_path; \
	echo "-- All rights reserved. This file and the source code it contains is" >> $$file_path; \
	echo "-- confidential and proprietary to Guias Scouts. No part of this" >> $$file_path; \
	echo "-- file may be reproduced, stored in a retrieval system, or transmitted" >> $$file_path; \
	echo "-- in any form or by any means, electronic, mechanical, photocopying," >> $$file_path; \
	echo "-- recording, or otherwise, without the prior written permission of" >> $$file_path; \
	echo "-- Guias Scouts." >> $$file_path; \
	echo "--" >> $$file_path; \
	echo "-- This file is provided \"as is\" with no warranties of any kind, express" >> $$file_path; \
	echo "-- or implied, including but not limited to, any implied warranty of" >> $$file_path; \
	echo "-- merchantability, fitness for a particular purpose, or non-infringement." >> $$file_path; \
	echo "-- In no event shall Guias Scouts be liable for any direct, indirect," >> $$file_path; \
	echo "-- incidental, special, exemplary, or consequential damages (including, but" >> $$file_path; \
	echo "-- not limited to, procurement of substitute goods or services; loss of use," >> $$file_path; \
	echo "-- data, or profits; or business interruption) however caused and on any" >> $$file_path; \
	echo "-- theory of liability, whether in contract, strict liability, or tort" >> $$file_path; \
	echo "-- (including negligence or otherwise) arising in any way out of the use" >> $$file_path; \
	echo "-- of this software, even if advised of the possibility of such damage." >> $$file_path; \
	echo "--" >> $$file_path; \
	echo "-- For licensing opportunities, please contact tropa92cr@gmail.com." >> $$file_path; \
	echo "File [$$file_path] Created"
