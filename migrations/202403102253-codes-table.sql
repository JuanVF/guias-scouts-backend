-- Copyright (c) 2024 Guias Scouts
--
-- All rights reserved. This file and the source code it contains is
-- confidential and proprietary to Guias Scouts. No part of this
-- file may be reproduced, stored in a retrieval system, or transmitted
-- in any form or by any means, electronic, mechanical, photocopying,
-- recording, or otherwise, without the prior written permission of
-- Guias Scouts.
--
-- This file is provided "as is" with no warranties of any kind, express
-- or implied, including but not limited to, any implied warranty of
-- merchantability, fitness for a particular purpose, or non-infringement.
-- In no event shall Guias Scouts be liable for any direct, indirect,
-- incidental, special, exemplary, or consequential damages (including, but
-- not limited to, procurement of substitute goods or services; loss of use,
-- data, or profits; or business interruption) however caused and on any
-- theory of liability, whether in contract, strict liability, or tort
-- (including negligence or otherwise) arising in any way out of the use
-- of this software, even if advised of the possibility of such damage.
--
-- For licensing opportunities, please contact tropa92cr@gmail.com.
USE `guias-scouts`;

CREATE TABLE t_codes_table (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(9) NOT NULL,
    created_at INT NOT NULL,
    id_user INT NOT NULL,
    FOREIGN KEY (id_user) REFERENCES t_users_table(id)
) ENGINE = InnoDB;