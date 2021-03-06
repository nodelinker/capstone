# Capstone Python bindings, by Nguyen Anh Quynnh <aquynh@gmail.com>

import ctypes, copy
from arm_const import *

# define the API
class ArmOpMem(ctypes.Structure):
    _fields_ = (
        ('base', ctypes.c_uint),
        ('index', ctypes.c_uint),
        ('scale', ctypes.c_int),
        ('disp', ctypes.c_int),
    )

class ArmOpShift(ctypes.Structure):
    _fields_ = (
        ('type', ctypes.c_uint),
        ('value', ctypes.c_uint),
    )

class ArmOpValue(ctypes.Union):
    _fields_ = (
        ('reg', ctypes.c_uint),
        ('imm', ctypes.c_int),
        ('fp', ctypes.c_double),
        ('mem', ArmOpMem),
    )

class ArmOp(ctypes.Structure):
    _fields_ = (
        ('shift', ArmOpShift),
        ('type', ctypes.c_uint),
        ('value', ArmOpValue),
    )

class CsArm(ctypes.Structure):
    _fields_ = (
        ('cc', ctypes.c_uint),
        ('update_flags', ctypes.c_bool),
        ('writeback', ctypes.c_bool),
        ('op_count', ctypes.c_uint8),
        ('operands', ArmOp * 20),
    )

def get_arch_info(a):
    return (a.cc, a.update_flags, a.writeback, copy.deepcopy(a.operands[:a.op_count]))

