# Basic BUND types
basic_Types = """
Model: n*=NameSpaceDef a*= AssignmentDef d *= DataDef;

NameSpaceDef:
    "[" name=NSID ">"
        ns*=NameSpaceDef
        statements*=AssignmentDef
    ";;"
;

AssignmentDef:
    DirectAssignmentDef | ReverseAssignmentDef | DirectLinkingDef | ReverseLinkingDef | DirectPythonDef | ReversePythonDef | DirectPipeDef | ReversePipeDef
;

DirectAssignmentDef:
    name=NameDef  DirectDataAssignmentOp data=DataDef
;

ReverseAssignmentDef:
    data=DataDef  ReverseDataAssignmentOp name=NameDef
;

DirectPythonDef:
    name=NameDef  DirectPythonAssignmentOp data=NameDef
;

ReversePythonDef:
    data=DataDef  ReversePythonAssignmentOp name=NameDef
;

DirectLinkingDef:
    name=NameDef  DirectLinkOp src=NSID
;

ReverseLinkingDef:
    src=NSID  ReverseLinkOp name=NameDef
;

DirectPipeDef:
    name=NameDef  DirectPipeOp def*=KV_TYPE[","]
;

ReversePipeDef:
    def*=KV_TYPE[","]  ReversePipeOp name=NameDef
;

NameDef:
    ID
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

DirectPythonAssignmentOp:
    "import" | "<-#"
;

ReversePythonAssignmentOp:
    "#->" | "to"
;

DirectLinkOp:
    "link" | "<-*"
;

ReverseLinkOp:
    "*->"
;

DirectPipeOp:
    "<pipe"
;

ReversePipeOp:
    "pipe>"
;

LIST_TYPE:
    "|" data *= DataDef[","] "|"
;

KV_TYPE:
    "{" name=NameDef  data=DataDef "}"
;

CODEWORD_REF_TYPE:
    ID | NSID | SPECIAL_TYPE | VERY_SPECIAL_TYPE
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

SPECIAL_TYPE:
    "+" | "-" | "++" | "--" | "<" | ">" | "==" | "=" | "<=" | "=>"
;

VERY_SPECIAL_TYPE:
    "===" | "+++" | "---" | "**" | "***"
;

DataDef:
    ID | BASETYPE | LIST_TYPE | KV_TYPE | LAMBDA_TYPE | REF_TYPE | CURRY_TYPE | PRELIMENARY_EXECUTE_TYPE | DO_EXECUTE_TYPE | NSID | SPECIAL_TYPE | VERY_SPECIAL_TYPE
;

Comment:
    /\\/\\*(.|\n)*?\\*\\//
;
"""
