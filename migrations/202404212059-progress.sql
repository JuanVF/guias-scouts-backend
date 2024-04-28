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

CREATE TABLE t_progress_type_table (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name NVARCHAR(40) NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

CREATE TABLE t_question_type_table (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name NVARCHAR(40) NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

CREATE TABLE t_progress_questions_table (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    question NVARCHAR(400) NOT NULL,
    id_question_type INT NOT NULL,
    id_progress_type INT NOT NULL,
    FOREIGN KEY (id_question_type) REFERENCES t_question_type_table(id),
    FOREIGN KEY (id_progress_type) REFERENCES t_progress_type_table(id)
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

CREATE TABLE t_protagonist_progress_table (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    question_id INT NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (question_id) REFERENCES t_progress_questions_table(id),
    FOREIGN KEY (user_id) REFERENCES t_users_table(id)
) ENGINE = InnoDB;

INSERT INTO
    t_progress_type_table (name)
VALUES
    ('Brújula Bronce'),
    ('Brújula Plata'),
    ('Brújula Oro'),
    ('Brújula Platino');

INSERT INTO
    t_question_type_table (name)
VALUES
    ('Guidismo y Escultismo'), -- 1
    ('Cabuyería'), -- 2
    ('Códigos y Claves'), -- 3
    ('Fuegos y Fogones'), -- 4
    ('Herramientas'), -- 5
    ('Campismo y Aire Libre'), -- 6
    ('Cocina y Nutrición'), -- 7 
    ('Acecho y Observación'), -- 8
    ('Comunicación'), -- 9
    ('Navegación Terrestre'), -- 10
    ('Salud y Seguridad'), -- 11
    ('Civismo'); -- 12
