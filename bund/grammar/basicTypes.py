# Basic BUND types
from textx import metamodel_from_str


basic_Types = """
Model: n+= AssignmentDef ;

AssignmentDef:
    DirectAssignmentDef | ReverseAssignmentDef
;

DirectAssignmentDef:
    name=NameDef  DirectDataAssignmentOp data=DataDef
;

ReverseAssignmentDef:
    data=DataDef  ReverseDataAssignmentOp name=NameDef
;

NameDef:
    ID | STRING
;

NSID:
    "/" ID ("/" ID)*
;

DirectDataAssignmentOp:
    "is" | "<-"
;

ReverseDataAssignmentOp:
    "->" | "as"
;

LIST_TYPE:
    "|" data *= DataDef[","] "|"
;

KV_TYPE:
    "{" name=NameDef  data=DataDef "}"
;

CODEWORD_REF_TYPE:
    ID | STRING | NSID
;

LAMBDA_TYPE:
    "(" words*= DataDef ")"
;

REF_TYPE:
    "`" data=DataDef
;

CURRY_TYPE:
    "(" name=CODEWORD_REF_TYPE "." value=DataDef ")"
;

DO_EXECUTE_TYPE:
    ";"
;

PRELIMENARY_EXECUTE_TYPE:
    ":" name=CODEWORD_REF_TYPE
;

DataDef:
    BASETYPE | LIST_TYPE | KV_TYPE | LAMBDA_TYPE | REF_TYPE | CURRY_TYPE | PRELIMENARY_EXECUTE_TYPE | DO_EXECUTE_TYPE | NSID
;
"""
