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

-- ---------------------------------------------------------------------------
--                   Brujula Bronce
-- ---------------------------------------------------------------------------

-- Inserting questions for 'Guidismo y Escultismo' category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Te has preguntado ¿Qué es el Escultismo y el Guidismo? Investiga para responder a esta pregunta', 1, 1),
    ('Explique cómo se conforma el Grupo Guía y Scout', 1, 1),
    ('Aprende y demuestra que vives el sentido de la Ley y de la Promesa Guía y Scout', 1, 1),
    ('Aprende el significado de la seña scouts', 1, 1),
    ('Aprende la Oración Guía y Scout', 1, 1),
    ('Aprende y demuestra que vives las Virtudes y los Principios Guías y Scout', 1, 1),
    ('Pídele a tu Guía de Patrulla que explique la historia de la Patrulla y de cómo funciona el Sistema de Patrulla', 1, 1),
    ('Narra la historia de la Asociación Guías y Scout de Costa Rica', 1, 1),
    ('Narra brevemente la historia del Movimiento', 1, 1),
    ('Narra el origen del apretón de manos scout', 1, 1),
    ('Aprende la seña Guía y Scout', 1, 1),
    ('Explica que es Lady Olave Saint-Clare Soames', 1, 1),
    ('Explica que son los Centros Mundiales Guías y cuáles son', 1, 1),
    ('Explique que es la Conferencia Scout Mundial y Boureau Scout Mundial', 1, 1);

-- Inserting questions for 'Cabuyería' category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Te Reto a realizar un cuadro de nudos y tipos de mecates', 2, 1),
    ('Demuestra que sabes aplicar los nudos de Riso y Arnés de hombre', 2, 1),
    ('Demostrar que sabes aplicar los siguientes nudos: vuelta escota simple, media llave, dos cotes y pescador', 2, 1),
    ('Demuestra que sabes aplicar los nudos de Margarita y el as de guía simple', 2, 1);

-- Inserting questions for 'Códigos y Claves' category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('¿Por qué no investigas cuáles son las claves de números y letras? Las aprendes y te inventas una para tu patrulla', 3, 1),
    ('Demuestra que sabes utilizar las siguientes claves: Murciélago, abuelito y gato', 3, 1),
    ('Demuestra que sabes utilizar la clave Hipotenusa', 3, 1);

-- Inserting questions for 'Fuegos y Fogones' category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Has encendido fuegos… los has apagado… Te reto a hacerlo, aprende las precauciones de seguridad, practícalo. Luego enséñaselo a tu Patrulla', 4, 1),
    ('Explicar qué elementos se requieren para el encendido del fuego', 4, 1),
    ('Demuestra que sabes encender el fuego utilizando yesca, astilla y combustibles', 4, 1),
    ('Conversa con tu Guía de Patrulla sobre las Normas de seguridad', 4, 1),
    ('Explica los usos que se le dan al fuego Tipi o Pirámide', 4, 1),
    ('Demuestra que sabes encender un fuego de Tipi o pirámide con las precauciones de seguridad', 4, 1);

-- Inserting questions for 'Herramientas' category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Antes que uses una herramienta debes saber las normas de seguridad, investiga… y aprende las normas de seguridad para el uso de las herramientas', 5, 1),
    ('Explícale a un miembro de tu patrulla cuáles son las normas de seguridad para utilizar herramientas', 5, 1),
    ('Demuestra cuáles son los usos correctos de la linterna', 5, 1),
    ('Demuestra que sabes utilizar una linterna de manera correcta', 5, 1),
    ('Conversa con tu Guías de Patrulla sobre las Normas de seguridad para el uso de las herramientas', 5, 1);

-- Inserting questions for 'Campismo y Aire Libre' category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Pídele a tu Guía de Patrulla la lista de artículos que debes llevar a una excursión y luego, que te ayude a revisar la forma en la que has acomodado tu mochila', 6, 1),
    ('Preséntate ante tu Guía de Patrulla antes de ir a Campamento y muéstrale que sabes preparar el Equipo personal de campamento', 6, 1),
    ('Demuestra cuáles son las medidas de seguridad a la hora de portar la mochila', 6, 1),
    ('Demuestra que sabes cuáles son las recomendaciones para el uso de calzado, ropa y el aseo personal en campamento', 6, 1),
    ('Explícale a tu patrulla cuál es el equipo de campismo y de cocina que se debe llevar a un campamento de dos noches y tres días', 6, 1),
    ('Explica cuáles son los cuidados que se deben tener con los medicamentos', 6, 1);

-- Inserting questions for 'Cocina y Nutrición' category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('¿Te has preguntado cómo se hace un buen menú para campamento? Apréndelos y verás que en la próxima excursión o campamento la pasarás muy bien', 7, 1),
    ('Demuestra que sabes cuál es la ubicación de la cocina en campamento', 7, 1),
    ('Cuáles son las medidas higiénicas que se debe tener en la cocina', 7, 1),
    ('Las medidas de seguridad con los utensilios de cocina', 7, 1),
    ('Cuidados que se deben tener con los utensilios personales para comer', 7, 1);

-- Inserting questions for 'Acecho y Observación' category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Has escuchado de las señales de pista, te has preguntado ¿Qué son? ¿Te gustaría saber cómo se utilizan? Investiga y aprende la técnica', 8, 1),
    ('Demuestra que sabes reconocer las señales de pista artificiales y naturales', 8, 1),
    ('Sigue una pista trazada con signos artificiales en el campo', 8, 1),
    ('Demuestra que sabes cuáles son las señales de pista', 8, 1),
    ('Sigue una pista trazada con señales de pista', 8, 1),
    ('Demuestra y explica cómo dejar señales de pistas en una ruta de rastreo', 8, 1);

-- Inserting questions for 'Comunicación' category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Te reto a conocer sobre internet y a que trabajes el programa mundial de Surf Smart y saques la especialidad de Redes o Internet', 9, 1),
    ('Conversa con tu Dirigente para obtener la especialidad de Redes o Internet', 9, 1),
    ('Conversa con tu Guía de Patrulla sobre la seguridad que se debe tener en la internet', 9, 1),
    ('Organiza para tu patrulla para trabajar la Insignia Surf Smart', 9, 1),
    ('Mencione las características que tienen internet para la vida diaria de las personas', 9, 1),
    ('Explique los siguientes servicios que se encuentran en la internet: Correo electrónico [e-mail], navegadores, buscadores, Jota Joti, Wikipedia, Comercio electrónico [E-comerce]', 9, 1);

-- Inserting questions for 'Navegación Terrestre' category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('¿Por dónde sale el sol? ¿Hacia dónde miran las puertas de las iglesias? ¿Sabes ubicarte en una ciudad? No… Investiga y aprende tips para poder orientarte en la ciudad', 10, 1),
    ('Con ayuda de tu Guía de Patrulla prepara una actividad sobre los puntos cardinales y aplicada en una Reunión de Patrulla', 10, 1),
    ('Demuestra con una brújula que las direcciones y los rumbos', 10, 1),
    ('Investiga qué otras formas se pueden utilizar que permiten orientarse', 10, 1),
    ('En Reunión de Patrulla explica al menos una forma de orientación que investigaste', 10, 1);

-- Inserting questions for 'Salud y Seguridad' category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Recuerda que los hábitos de higiene son muy importantes, su principal objetivo es cuidarte. Prepárate, aprende cuáles son y aplícalos en tu vida', 11, 1),
    ('Explique por qué se debe dormir el tiempo suficiente', 11, 1),
    ('Demuestra y organiza tu tiempo para el descanso necesario', 11, 1),
    ('Aprende y practica las reglas básicas de higiene para: cuidar tu cuerpo; La piel, los dientes, los ojos, los oídos y los pulmones', 11, 1);

-- Inserting questions for 'Civismo' category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Es importante que conozcas los símbolos nacionales, su historia, cuando los declararon símbolos nacionales, y lo más importante, es saber su verdadero significado para los costarricenses. Prepárate y aprende', 12, 1),
    ('Describa la Bandera de Costa Rica', 12, 1),
    ('Explica por qué y demuestra cómo debe respetarse la Bandera', 12, 1),
    ('Demuestra que sabes izar y arrear de la bandera', 12, 1),
    ('Explica por qué y demuestra cómo doblar la bandera', 12, 1),
    ('Explica por qué y demuestra cuál es la forma correcta para que ondee la bandera', 12, 1);


-- ---------------------------------------------------------------------------
--                   Brujula Plata
-- ---------------------------------------------------------------------------

-- Inserting questions for 'Guidismo y Escultismo' for Brújula Plata category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Te has preguntado ¿Qué es el Escultismo y el Guidismo? Investiga para responder a esta pregunta', 1, 2),
    ('Explique cómo se conforma el Grupo Guía y Scout', 1, 2),
    ('Aprende y demuestra que vives el sentido de la Ley y de la Promesa Guía y Scout', 1, 2),
    ('Aprende el significado de la seña scouts', 1, 2),
    ('Aprende la Oración Guía y Scout', 1, 2),
    ('Aprende y demuestra que vives las Virtudes y los Principios Guías y Scout', 1, 2),
    ('Pídele a tu Guía de Patrulla que explique la historia de la Patrulla y de cómo funciona el Sistema de Patrulla', 1, 2),
    ('Narra la historia de la Asociación Guías y Scout de Costa Rica', 1, 2),
    ('Narra brevemente la historia del Movimiento', 1, 2),
    ('Narra el origen del apretón de manos scout', 1, 2),
    ('Aprende la seña Guía y Scout', 1, 2),
    ('Explica que es Lady Olave Saint-Clare Soames', 1, 2),
    ('Explica que son los Centros Mundiales Guías y cuáles son', 1, 2),
    ('Explique que es la Conferencia Scout Mundial y Boureau Scout Mundial', 1, 2);

-- Inserting questions for 'Cabuyería' for Brújula Plata category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('¡Será de cabuya o de algodón! Investiga, cuáles son las mejores cuerdas para realizar los nudos', 2, 2),
    ('Demuestra que sabes aplicar los nudos Ballestrinque simple y ballestrinque doble', 2, 2),
    ('Demuestra que sabes aplicar los nudos vuelta de Brasa y De silla de bomberos', 2, 2);

-- Inserting questions for 'Códigos y Claves' for Brújula Plata category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Hay claves muy sencillas y otros más complejas ¿Por qué no investigas y los practicas en juegos con tu patrulla?', 3, 2),
    ('Demuestra que sabes utilizar las siguientes claves: Cenit Polar y neumático', 3, 2),
    ('Demuestra que sabes utilizar las siguientes claves: paralinofu y china', 3, 2),
    ('Demuestra que sabes utilizar las siguientes claves numérica: Alfabeto al revés', 3, 2),
    ('Enséñale a un miembro nuevo de tu patrulla el uso de estas claves', 3, 2);

-- Inserting questions for 'Fuegos y Fogones' for Brújula Plata category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Si ya conoces la seguridad para los fogones de campamento ¡Genial! De no ser así, te reto… investiga y prepara una charla práctica a tu patrulla', 4, 2),
    ('En reunión de Patrulla explica cuáles son las medidas de seguridad que se debe tener con los fuegos', 4, 2),
    ('Conversa con tu Dirigente para obtener la especialidad de Bombero', 4, 2),
    ('Haz una demostración a tu patrulla, como se debe mantener la leña en campamento y en el local', 4, 2),
    ('Explica los usos que se le dan al fuego de consejo o cruzado', 4, 2),
    ('Demuestra que sabes encender un fuego de consejo o cruzado con las precauciones de seguridad', 4, 2);

-- Inserting questions for 'Herramientas' for Brújula Plata category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Por qué no obtienes alguna de estas especialidades: Cuidado de herramientas o uso y seguridad de herramientas', 5, 2),
    ('Conversa con tu Dirigente para obtener la especialidad de Cuidados de Herramientas o uso y seguridad de herramientas', 5, 2),
    ('Demuestra que sabes utilizar la navaja de bolsillo', 5, 2);

-- Inserting questions for 'Campismo y Aire Libre' for Brújula Plata category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Prepara tu mochila, considerando las características corporales y luego pídele a tu Guía de Patrulla que te revise la mochila ya preparada… ¡Haz tus anotaciones!', 6, 2),
    ('Explica en Reunión de Patrulla cuales son las recomendaciones que deben tener para comprar una mochila', 6, 2),
    ('Haz una demostración a tu patrulla cual es la forma correcta de empacar la mochila de campamento', 6, 2),
    ('Demuestra que sabes portar correctamente una mochila de excursión y de campamento', 6, 2);

-- Inserting questions for 'Cocina y Nutrición' for Brújula Plata category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Demuestra a la Patrulla que puedes hacerte cargo y mantener en buen estado el equipo en la patrulla. Mejor aún, pide ser el Intendente de la Patrulla', 7, 2),
    ('Conversa con tu Dirigente y obtén la especialidad de Cocina', 7, 2),
    ('Explícale a un miembro nuevo de la patrulla cuál es el equipo personal de cocina y cuáles son las medidas higiénicas que se debe tener', 7, 2),
    ('Conversa con tu Guía de Patrulla y explícale cuál es la relación que tiene el menú con el equipo de cocina', 7, 2);

-- Inserting questions for 'Acecho y Observación' for Brújula Plata category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('¿Conoces alguna de las técnicas de rastreo? Investiga, práctica y enséñale a tu patrulla', 8, 2),
    ('Investiga quién era Joseph Rudyard Kipling y coméntalo con la Patrulla', 8, 2),
    ('Prepara una charla para tu Patrulla sobre la historia de Kim', 8, 2),
    ('Investiga y enséñale a tu patrulla una técnica de rastreo', 8, 2),
    ('En una salida de patrulla, saca una huella en yeso', 8, 2),
    ('Explícale a un miembro nuevo de tu patrulla, como es la huella que deja el animal emblema de patrulla', 8, 2);

-- Inserting questions for 'Comunicación' for Brújula Plata category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Ahora navegamos en las redes sociales, principalmente en FACEBOOK, pero son muchos los riesgos que se corre. Te reto a conocer sobre las Redes Sociales y aprender las Netiquetas', 9, 2),
    ('Investiga sobre las Redes Sociales, escoge una de ellas (Facebook, YouTube, Twitter, Instagram, Snapchat, entre otras) y prepara una charla para tu patrulla, explicándoles el uso de la Red social escogida (positivo y negativo), medidas de seguridad', 9, 2);

-- Inserting questions for 'Navegación Terrestre' for Brújula Plata category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Te reto a sacar la especialidad de Navegación terrestre, orientación o lectura de mapas', 10, 2),
    ('Obtén la especialidad de Navegación Terrestre', 10, 2),
    ('Demuestra que sabes utilizar la Rosa de los Vientos', 10, 2),
    ('Participa en una demostración de cómo orientarse por medio del sol', 10, 2),
    ('Demuestra que sabes utilizar la brújula Lensática', 10, 2),
    ('Investiga los tipos de brújulas que existen y aprende a utilizar la brújula cartográfica o de rejilla', 10, 2),
    ('Demuestra que sabes cuáles son los cuidados de una brújula a la hora de guardarla y el momento de utilizarla', 10, 2),
    ('Aprende a orientarte por medio del método del reloj, método de la sombra, método de sombras iguales y encontrar direcciones utilizando la luna', 10, 2);

-- Inserting questions for 'Salud y Seguridad' for Brújula Plata category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Investiga y aprende los pasos del Método de los Primeros Auxilios', 11, 2),
    ('Investiga qué son los primeros auxilios', 11, 2),
    ('Obtén la especialidad de Preparación de emergencias', 11, 2),
    ('Demuestra que mantienes un botiquín personal de primeros auxilios', 11, 2),
    ('Promueve una actividad para tu patrulla y obtener artículos para el Botiquín de patrulla', 11, 2),
    ('Explica cuáles y por qué son los artículos que se debe tener en un Botiquín de Tropa', 11, 2);

-- Inserting questions for 'Civismo' for Brújula Plata category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Investiga sobre la Cruz Roja de tu comunidad ¿Qué hacen? ¿Qué puedes hacer para ayudar a la Cruz Roja? Diseña un proyecto sobre cómo puedes ayudar y ejecútalo con tu patrulla', 12, 2),
    ('Obtén la especialidad de Civismo y servicio a la comunidad', 12, 2),
    ('Explica la importancia que tiene la Cruz Roja para los costarricenses', 12, 2),
    ('Explícale a un miembro nuevo de la patrulla la historia de la Cruz Roja', 12, 2);

-- ---------------------------------------------------------------------------
--                   Brujula Oro
-- ---------------------------------------------------------------------------

-- Inserting questions for 'Guidismo y Escultismo' for Brújula Oro category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Te has preguntado ¿Qué es el Escultismo y el Guidismo? Investiga para responder a esta pregunta', 1, 3),
    ('Explique cómo se conforma el Grupo Guía y Scout', 1, 3),
    ('Aprende y demuestra que vives el sentido de la Ley y de la Promesa Guía y Scout', 1, 3),
    ('Aprende el significado de la seña scouts', 1, 3),
    ('Aprende la Oración Guía y Scout', 1, 3),
    ('Aprende y demuestra que vives las Virtudes y los Principios Guías y Scout', 1, 3),
    ('Pídele a tu Guía de Patrulla que explique la historia de la Patrulla y de cómo funciona el Sistema de Patrulla', 1, 3),
    ('Narra la historia de la Asociación Guías y Scout de Costa Rica', 1, 3),
    ('Narra brevemente la historia del Movimiento', 1, 3),
    ('Narra el origen del apretón de manos scout', 1, 3),
    ('Aprende la seña Guía y Scout', 1, 3),
    ('Explica que es Lady Olave Saint-Clare Soames', 1, 3),
    ('Explica que son los Centros Mundiales Guías y cuáles son', 1, 3),
    ('Explique que es la Conferencia Scout Mundial y Boureau Scout Mundial', 1, 3);

-- Inserting questions for 'Cabuyería' for Brújula Oro category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Obtén la especialidad de Cuidados de cuerdas y mecates', 2, 3),
    ('Demuestra que sabes aplicar los nudos presilla de alondra y nudo aguja y cabeza de turco', 2, 3),
    ('Conversa con tu Dirigente para obtener la especialidad de Pionerismo', 2, 3),
    ('Demuestra el uso práctico de los siguientes nudos: Eslinga y remate refuerzo de cabo', 2, 3);

-- Inserting questions for 'Códigos y Claves' for Brújula Oro category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Investiga sobre las claves de números, aprende una y enséñala a tu patrulla', 3, 3),
    ('Aprende la clave siete cruces y enséñasela a tu patrulla o a un miembro nuevo de la patrulla o la tropa', 3, 3),
    ('Aprende las claves musical y bailarín y explica su aplicación', 3, 3);

-- Inserting questions for 'Fuegos y Fogones' for Brújula Oro category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Aprende a construir los siguientes fuegos: fogón de estrella, fuego de cazador, fogón de roca, fuego de tres piedras y fogón de polinesio', 4, 3),
    ('Escoge dos tipos de fuegos y explícale a tu patrulla cómo se construyen y los beneficios para campamento', 4, 3),
    ('Utilizando el fuego de roca, prepara una comida para tu patrulla', 4, 3),
    ('Realiza una demostración con uno de los siguientes fogones: el de tres piedras y el polinesio', 4, 3);

-- Inserting questions for 'Herramientas' for Brújula Oro category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Obtén la especialidad de Medidas de seguridad con herramientas', 5, 3),
    ('Conversa con tu Guía de Patrulla y explícale cómo se debe utilizar la Navaja', 5, 3),
    ('Realiza una demostración de cómo se debe utilizar el Machete', 5, 3);

-- Inserting questions for 'Campismo y Aire Libre' for Brújula Oro category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Organiza un campamento modelo durante una reunión de patrulla', 6, 3),
    ('Demuestra que sabes cuidar una tienda de campaña', 6, 3),
    ('Demuestra que sabes las características de las tiendas de campaña y cómo elegir la idónea para un campamento', 6, 3),
    ('Investiga sobre los tipos de tiendas de campaña, elige una de estas y enséñale a tu patrulla cómo se arma y se desarma la tienda', 6, 3),
    ('Investiga sobre los refugios naturales y artificiales, y pasa una noche en uno', 6, 3);

-- Inserting questions for 'Cocina y Nutrición' for Brújula Oro category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Aprende a cocinar y planea un concurso en donde participe la patrulla, a toda la tropa. Sería genial un Master Chef de Patrulla', 7, 3),
    ('Realiza una entrevista a un nutricionista sobre la importancia de la nutrición y la rueda de la nutrición', 7, 3),
    ('Elabora un boletín digital sobre el tema y envíalo a todos tus compañeros de patrulla', 7, 3),
    ('Busca la ayuda de un nutricionista y prepara una charla para tu patrulla de cómo preparar un menú balanceado. Pídele ayuda a tu Dirigente', 7, 3),
    ('Prepara el menú para el próximo campamento de patrulla o de tropa, que tenga desayunos, meriendas, almuerzos, postres, cenas. Considera la tabla de porciones', 7, 3),
    ('Obtén el presupuesto y las cuotas por cada miembro de la patrulla', 7, 3);

-- Inserting questions for 'Acecho y Observación' for Brújula Oro category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Sabes... ¿observar al dirigente sin que te vean? ¿Jugar asalto al Banderín? Investiga y aprende algunos juegos que podrás poner en práctica en el próximo campamento de patrulla o en la tropa', 8, 3),
    ('Investiga sobre los siguientes juegos de acecho: El pirata dormido, lobo precavido, acechando al venado, Patrulla contra patrulla, pueden ser otros. Escoge uno y practícalo con tu patrulla', 8, 3),
    ('Completa la tabla sobre las dimensiones de tu cuerpo (pág. 70) de la Brújula de Oro', 8, 3),
    ('Obtén una o varias especialidades de entre: botánica, biogeografía, uso de plantas medicinales, ornitología, identificación de aves, ecología, entomología, geología y geografía', 8, 3);

-- Inserting questions for 'Comunicación' for Brújula Oro category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Obtén una de las siguientes especialidades: Internet, redes sociales, informática, comunicaciones', 9, 3),
    ('Escoge alguna de las siguientes herramientas y prepara un taller para la patrulla o alguna de las secciones del grupo: Internet, correo electrónico, chat, blog o microblog, Tablet, telefonía fija y móvil, foros', 9, 3),
    ('Prepara una videoconferencia con un especialista nacional o internacional para tu patrulla, sobre un tema Guía y Scout que tu escojas', 9, 3);

-- Inserting questions for 'Navegación Terrestre' for Brújula Oro category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Vamos a dibujar un pequeño mapa del pueblo donde vivimos, pero usando la simbología topográfica', 10, 3),
    ('Prepara una charla práctica para tu patrulla de cómo leer una hoja topográfica', 10, 3),
    ('Usando una brújula, sigue una ruta establecida con tres diferentes lecturas en grados y tres diferentes distancias', 10, 3),
    ('Aprende cómo obtener un rumbo y haz una demostración a tu patrulla', 10, 3);

-- Inserting questions for 'Salud y Seguridad' for Brújula Oro category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Busca ayuda en el puesto de Cruz Roja o con los paramédicos para que puedan recibir un taller o curso de primeros auxilios', 11, 3),
    ('Demuestras que sabes cómo se debe trasladar a un herido', 11, 3),
    ('Demuestra cómo tratar hemorragias nasales, espinas, plantas tóxicas cortadas, raspaduras leves, ampollas', 11, 3),
    ('Demuestra cómo hacer los vendajes de cabeza, dedo, mano, muñeca, brazo (cabestrillo) tobillo, pie, muñeca y explica su aplicación', 11, 3),
    ('Demuestra que sabes identificar fracturas simples y compuestas. Demuestra el tratamiento de fracturas simples', 11, 3),
    ('Explica cómo se deben realizar las inmovilizaciones de: costilla, clavícula, pelvis, cadera y fémur', 11, 3);

-- Inserting questions for 'Civismo' for Brújula Oro category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('¡En tu comunidad hay lugares en los que puedes ayudar como Guía y Scout? Analiza tu comunidad y diseña un proyecto con tu patrulla sobre cómo pueden ayudar', 12, 3),
    ('Obtén la especialidad de Servicio a la Comunidad', 12, 3),
    ('Aprende a diseñar un proyecto Guía y Scout, utiliza el formato', 12, 3),
    ('Investiga sobre los bomberos de tu comunidad y prepara una actividad para tu patrulla o sección de tu Grupo', 12, 3);

-- ---------------------------------------------------------------------------
--                   Brujula Platino
-- ---------------------------------------------------------------------------

-- Inserting questions for 'Guidismo y Escultismo' for Brújula Platino category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Investiga y responde ¿Qué es el Escultismo y el Guidismo?', 1, 4),
    ('Explica cómo se conforma el Grupo Guía y Scout', 1, 4),
    ('Vive el sentido de la Ley y de la Promesa Guía y Scout', 1, 4),
    ('Aprende y demuestra el significado de la seña scouts', 1, 4),
    ('Aprende la Oración Guía y Scout', 1, 4),
    ('Vive las Virtudes y los Principios Guías y Scout', 1, 4),
    ('Explora la historia de la Patrulla y el Sistema de Patrulla', 1, 4),
    ('Narra la historia de la Asociación Guías y Scout de Costa Rica', 1, 4),
    ('Explora la historia del Movimiento Scout', 1, 4),
    ('Aprende sobre el origen del apretón de manos scout', 1, 4),
    ('Aprende la seña Guía y Scout', 1, 4),
    ('Explora quién fue Lady Olave Saint-Clare Soamos', 1, 4),
    ('Investiga sobre la Asociación Mundial Guía y Scout y los Centros Mundiales Guías', 1, 4),
    ('Explica la importancia de la Conferencia Scout Mundial y el Bureau Scout Mundial', 1, 4);

-- Inserting questions for 'Cabuyería' for Brújula Platino category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Obtén la especialidad de Pionerismo', 2, 4),
    ('Demuestra la aplicación de los amarres de cuadrado, diagonal y redondo', 2, 4),
    ('Demuestra la aplicación del amarre de Trípode', 2, 4);

-- Inserting questions for 'Códigos y Claves' for Brújula Platino category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Construye un zambador de morse con piezas de lata, baterías y tornillos', 3, 4),
    ('Investiga y explica las características de las claves de signos, sonidos y banderines', 3, 4),
    ('Transmite un mensaje sin hablar o escribir usando el código morse o el semáforo', 3, 4),
    ('Explica cómo se utiliza la clave mnemotécnica gráfica', 3, 4);

-- Inserting questions for 'Fuegos y Fogones' for Brújula Platino category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Prepara una exposición sobre los diferentes tipos de fuegos que conoces', 4, 4),
    ('Aprende y demuestra cómo hacer los siguientes tipos de fuego: reflector, altar triangular, de corredor. Escoge uno y prepara un almuerzo o cena para tu patrulla', 4, 4),
    ('Explora el impacto ambiental que pueden tener los fuegos y conversa al respecto con tu guía de patrulla', 4, 4),
    ('Obtén la especialidad de Cocina', 4, 4),
    ('Realiza una actividad para tu patrulla donde enseñes cómo hacer un fogón de altar en miniatura utilizando materiales como plastilina, pinchos y manila', 4, 4);

-- Inserting questions for 'Herramientas' for Brújula Platino category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Sirve a tu patrulla como Intendente de la Patrulla', 5, 4),
    ('Demuestra durante el próximo campamento el uso correcto del hacha de mano, pala plegable o palín, sierra de arco, rabo de zorro y el mazo', 5, 4),
    ('Obtén la especialidad de "Uso de herramientas"', 5, 4),
    ('Explica a un scout o una guía nueva cuáles son las medidas de seguridad para utilizar las herramientas', 5, 4);

-- Inserting questions for 'Campismo y Aire Libre' for Brújula Platino category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Ayuda a tu patrulla a planificar las construcciones para el próximo campamento, calculando la cantidad de materiales y el presupuesto', 6, 4),
    ('Asiste a tu Guía de Patrulla en la preparación y realización de la reunión de patrulla de la próxima semana', 6, 4),
    ('Planifica un campamento de al menos 3 días para tu patrulla y realiza varias actividades relacionadas, incluyendo la planificación, la preparación del menú, la organización del programa y la distribución del campamento', 6, 4),
    ('Explica en una reunión de patrulla cómo se debe organizar un campamento de patrulla, incluyendo la importancia de las construcciones de campamento', 6, 4),
    ('Diseña una actividad de patrulla donde enseñes la distribución del rincón de patrulla en un campamento', 6, 4);

-- Inserting questions for 'Cocina y Nutrición' for Brújula Platino category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Obtén al menos una de las siguientes especialidades: supervivencia en la naturaleza, cocina sin utensilios, preparación de postres, cocina de campamento', 7, 4),
    ('Investiga y presenta a tu patrulla las diferentes formas de almacenar alimentos en campamento y en la ciudad, incluyendo consejos y recomendaciones', 7, 4),
    ('Cocina al menos cinco alimentos sin utensilios', 7, 4),
    ('Da una demostración a tu patrulla de cómo hervir, guisar, freír, asar y asar a la parrilla', 7, 4),
    ('Realiza un taller de cocina sin utensilios con tu patrulla utilizando hojas verdes, barro o arcilla, y cáscaras', 7, 4),
    ('Explica a tu patrulla las técnicas de barro y horno de barro de pozo', 7, 4);

-- Inserting questions for 'Acecho y Observación' for Brújula Platino category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Visita el Sistema Nacional de Áreas de Conservación (SINAC), averigua sobre un área silvestre protegida, organiza una excursión para tu patrulla o tropa y actúa como guía, compartiendo la información que obtuviste', 8, 4),
    ('Obtén una especialidad de servicio forestal, zoología, ornitología o zonas comunes recreativas', 8, 4),
    ('Prepara una charla para tu patrulla sobre áreas silvestres protegidas, áreas de conservación, parques nacionales, reservas y áreas protegidas', 8, 4),
    ('Selecciona un parque, refugio o zona protegida, organiza una excursión con tu patrulla, actúa como guía y prepara un informe de la actividad para el libro de oro', 8, 4);

-- Inserting questions for 'Comunicación' for Brújula Platino category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Crea un álbum digital del próximo campamento de tu patrulla utilizando un programa como Microsoft Photo Story, Hotman Digital Álbum o Fotoprix Fotolibro', 9, 4),
    ('Obtén las especialidades de fotografía, diseño gráfico y periodismo', 9, 4),
    ('Graba un video con tu smartphone de una actividad de patrulla y compártelo en la red social de tu patrulla, tu tropa o tu grupo', 9, 4),
    ('Realiza un proyecto de una actividad de comunicación, como un taller de fotografía, la visita de un fotógrafo a una actividad de patrulla, una charla sobre reglas básicas para fotografía correcta o un taller sobre cómo compartir fotografías de manera segura', 9, 4);

-- Inserting questions for 'Navegación Terrestre' for Brújula Platino category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Aprende a hacer un croquis y realiza uno en la próxima caminata de tu patrulla, firma con tu rúbrica scouts y pégalos en el libro de oro', 10, 4),
    ('Investiga sobre herramientas digitales para orientación (app), escoge una y realiza una demostración a tu patrulla sobre cómo utilizarla', 10, 4),
    ('Dibuja un croquis de una zona amplia utilizando símbolos topográficos para demostrar tu habilidad en la elaboración de croquis o bocetos de mapas', 10, 4),
    ('Elige un navegador GPS de los mencionados en la brújula y prepara un taller para tu patrulla sobre cómo utilizarlo eficientemente', 10, 4);

-- Inserting questions for 'Salud y Seguridad' for Brújula Platino category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Prepara un proyecto para llevar a cabo una campaña de concientización en tu barrio para que todos estén preparados para emergencias', 11, 4),
    ('Da una charla en tu colegio o en alguna sección del grupo sobre cómo actuar en algún caso de emergencia, como movimientos sísmicos, huracanes, inundaciones, erupciones volcánicas, accidentes de tránsito, incendios, etc.', 11, 4),
    ('Explica qué es el triángulo de vida', 11, 4),
    ('Demuestra qué contiene una mochila de emergencia y asegúrate de que haya una en tu casa', 11, 4);

-- Inserting questions for 'Civismo' for Brújula Platino category
INSERT INTO t_progress_questions_table (question, id_question_type, id_progress_type)
VALUES
    ('Prepara un video con la ayuda de tu patrulla y compártelo en internet y en redes sociales sobre una entidad autónoma de nuestro país', 12, 4),
    ('Plantea un proyecto relacionado con la limpieza de señales de tránsito, colocación de una nueva señal de tránsito o una campaña de seguridad vial', 12, 4),
    ('Capacita a una sección del grupo sobre seguridad vial', 12, 4),
    ('Investiga sobre una entidad autónoma de nuestro país, su importancia y cómo ayuda a la población civil, luego conversa con tu Guía de Patrulla sobre tu investigación', 12, 4);
