/*
Navicat SQLite Data Transfer

Source Server         : REAL
Source Server Version : 30714
Source Host           : :0

Target Server Type    : SQLite
Target Server Version : 30714
File Encoding         : 65001

Date: 2017-05-17 10:15:09
*/

PRAGMA foreign_keys = OFF;

-- ----------------------------
-- Table structure for cuentas_estado_solicitud
-- ----------------------------
DROP TABLE IF EXISTS "main"."cuentas_estado_solicitud";
CREATE TABLE "cuentas_estado_solicitud" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "tipo_solicitud" varchar(30) NOT NULL);

-- ----------------------------
-- Records of cuentas_estado_solicitud
-- ----------------------------
INSERT INTO "main"."cuentas_estado_solicitud" VALUES (1, 'en proceso');
INSERT INTO "main"."cuentas_estado_solicitud" VALUES (2, 'en evaluación');
INSERT INTO "main"."cuentas_estado_solicitud" VALUES (3, 'aprobada');
INSERT INTO "main"."cuentas_estado_solicitud" VALUES (4, 'no aprobada');
