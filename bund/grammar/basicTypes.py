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
    ID | SPECIAL_TYPE
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
    "link" | "<link"
;

ReverseLinkOp:
    "link>"
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
    ID | NSID | SPECIAL_TYPE
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

ANY_PLUS:
    /(\+)+/
;
ANY_MINUS:
    /(\-)+/
;
ANY_MORE:
    /(\>)+/
;
ANY_LESS:
    /(\<)+/
;
ANY_STAR:
    /(\*)+/
;
ANY_EQ:
    /(\=)+/
;
ANY_PERCENT:
    /\%/
;
ANY_COMBO:
    /(\+|\=|\<|\>|\?|\!|\-|\*)+(\+|\=|\<|\>|\?|\!|\-|\*)+/
;
ANY_TRIPLE:
    /(\+|\-|\*|\=|\<|\>|\?|\!)+(\=|\<|\>|\?|\!|\*)+(\+|\-|\=|\<|\>|\?|\!|\*)+/
;

SPECIAL_TYPE:
    ANY_COMBO | ANY_TRIPLE | ANY_STAR | ANY_PERCENT | ANY_MINUS | ANY_MORE | ANY_LESS | ANY_EQ | ANY_PLUS 
;

DataDef:
    ID | BASETYPE | LIST_TYPE | KV_TYPE | LAMBDA_TYPE | REF_TYPE | CURRY_TYPE | PRELIMENARY_EXECUTE_TYPE | DO_EXECUTE_TYPE | NSID | SPECIAL_TYPE
;

Comment:
    /\\/\\*(.|\n)*?\\*\\//
;
"""
