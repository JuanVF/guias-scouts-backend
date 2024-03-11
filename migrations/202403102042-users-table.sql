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
-- Create t_users_table
USE `guias-scouts`;

CREATE TABLE t_users_table (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    id_patrol INT,
    email VARCHAR(120) NOT NULL,
    birthday INT NOT NULL,
    password VARCHAR(512) NOT NULL,
    active TINYINT(1) NOT NULL,
    created_at INT NOT NULL,
    id_role INT NOT NULL,
    FOREIGN KEY (id_patrol) REFERENCES t_patrols_table(id),
    FOREIGN KEY (id_role) REFERENCES t_roles_table(id)
) ENGINE = InnoDB;

INSERT INTO
    t_users_table (
        fullname,
        email,
        birthday,
        password,
        active,
        created_at,
        id_role
    )
VALUES
    (
        'root',
        'root@scouts.com',
        983923200,
        '8cd824c700eb0c125fff40c8c185d14c5dfe7f32814afac079ba7c20d93bc3c082193243c420fed22ef2474fbb85880e7bc1ca772150a1f759f8ddebca77711f',
        1,
        1710128864,
        1
    );