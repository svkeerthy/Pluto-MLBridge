# Pluto
#
# Copyright (C) Uday Bondhugula 2007
#

SUBDIRS = 

MAINTAINERCLEANFILES = Makefile.in


if EXTERNAL_ISL
# ISL_INCLUDE, ISL_LIBADD were already defined
else
ISL_INCLUDE += -I$(top_srcdir)/isl/include
ISL_LIBADD += $(top_srcdir)/isl/libisl.la
endif

bin_PROGRAMS = pluto

pluto_SOURCES = constraints.c constraints_polylib.c constraints_isl.c math_support.c ddg.c transforms.c pluto.c post_transform.c framework.c pluto_codegen_if.c polyloop.c ast_transform.c iss.c main.c constraints.h math_support.h pluto.h program.c program.h tile.c unit_tests.c

if PLUTO_DEBUG
OPT_FLAGS = 
DEBUG_FLAGS = -g
else
OPT_FLAGS = -O3 -funroll-loops -fopenmp
endif

pluto_CPPFLAGS = $(OPT_FLAGS) $(DEBUG_FLAGS) -funroll-loops -fopenmp \
   -DSCOPLIB_INT_T_IS_LONGLONG -DCLOOG_INT_GMP \
   -I../include \
   -I../piplib/include \
   -I../clan/include \
   $(ISL_INCLUDE) \
   -I../cloog-isl/include \
   -I../openscop/include \
   -I../candl/include \
   -I../polylib/include \
   -I/home/cs20btech11018/repos/MLCompilerBridge/include

pluto_LDFLAGS = -static -fopenmp  -L/home/mlbridge/AEInstall/MLCompilerBridge_Install -lMLCompilerBridgeC -L/home/mlbridge/.local/onnxruntime-linux-x64-gpu-1.14.0/lib -lonnxruntime -lstdc++ -L/usr/lib/llvm-10/lib -lLLVMXRay -lLLVMWindowsManifest -lLLVMTableGen -lLLVMSymbolize -lLLVMDebugInfoPDB -lLLVMPerfJITEvents -lLLVMOrcJIT -lLLVMOrcError -lLLVMJITLink -lLLVMObjectYAML -lLLVMMCA -lLLVMLTO -lLLVMObjCARCOpts -lLLVMPasses -lLLVMLineEditor -lLLVMLibDriver -lLLVMInterpreter -lLLVMFuzzMutate -lLLVMFrontendOpenMP -lLLVMMCJIT -lLLVMExecutionEngine -lLLVMRuntimeDyld -lLLVMDWARFLinker -lLLVMDlltoolDriver -lLLVMOption -lLLVMDebugInfoGSYM -lLLVMCoverage -lLLVMCoroutines -lLLVMAVRDisassembler -lLLVMAVRCodeGen -lLLVMAVRAsmParser -lLLVMAVRDesc -lLLVMAVRInfo -lLLVMXCoreDisassembler -lLLVMXCoreCodeGen -lLLVMXCoreDesc -lLLVMXCoreInfo -lLLVMX86Disassembler -lLLVMX86AsmParser -lLLVMX86CodeGen -lLLVMX86Desc -lLLVMX86Utils -lLLVMX86Info -lLLVMWebAssemblyDisassembler -lLLVMWebAssemblyCodeGen -lLLVMWebAssemblyDesc -lLLVMWebAssemblyAsmParser -lLLVMWebAssemblyInfo -lLLVMSystemZDisassembler -lLLVMSystemZCodeGen -lLLVMSystemZAsmParser -lLLVMSystemZDesc -lLLVMSystemZInfo -lLLVMSparcDisassembler -lLLVMSparcCodeGen -lLLVMSparcAsmParser -lLLVMSparcDesc -lLLVMSparcInfo -lLLVMRISCVDisassembler -lLLVMRISCVCodeGen -lLLVMRISCVAsmParser -lLLVMRISCVDesc -lLLVMRISCVUtils -lLLVMRISCVInfo -lLLVMPowerPCDisassembler -lLLVMPowerPCCodeGen -lLLVMPowerPCAsmParser -lLLVMPowerPCDesc -lLLVMPowerPCInfo -lLLVMNVPTXCodeGen -lLLVMNVPTXDesc -lLLVMNVPTXInfo -lLLVMMSP430Disassembler -lLLVMMSP430CodeGen -lLLVMMSP430AsmParser -lLLVMMSP430Desc -lLLVMMSP430Info -lLLVMMipsDisassembler -lLLVMMipsCodeGen -lLLVMMipsAsmParser -lLLVMMipsDesc -lLLVMMipsInfo -lLLVMLanaiDisassembler -lLLVMLanaiCodeGen -lLLVMLanaiAsmParser -lLLVMLanaiDesc -lLLVMLanaiInfo -lLLVMHexagonDisassembler -lLLVMHexagonCodeGen -lLLVMHexagonAsmParser -lLLVMHexagonDesc -lLLVMHexagonInfo -lLLVMBPFDisassembler -lLLVMBPFCodeGen -lLLVMBPFAsmParser -lLLVMBPFDesc -lLLVMBPFInfo -lLLVMARMDisassembler -lLLVMARMCodeGen -lLLVMARMAsmParser -lLLVMARMDesc -lLLVMARMUtils -lLLVMARMInfo -lLLVMAMDGPUDisassembler -lLLVMAMDGPUCodeGen -lLLVMMIRParser -lLLVMipo -lLLVMInstrumentation -lLLVMVectorize -lLLVMLinker -lLLVMIRReader -lLLVMAsmParser -lLLVMAMDGPUAsmParser -lLLVMAMDGPUDesc -lLLVMAMDGPUUtils -lLLVMAMDGPUInfo -lLLVMAArch64Disassembler -lLLVMMCDisassembler -lLLVMAArch64CodeGen -lLLVMCFGuard -lLLVMGlobalISel -lLLVMSelectionDAG -lLLVMAsmPrinter -lLLVMDebugInfoDWARF -lLLVMCodeGen -lLLVMTarget -lLLVMScalarOpts -lLLVMInstCombine -lLLVMAggressiveInstCombine -lLLVMTransformUtils -lLLVMBitWriter -lLLVMAnalysis -lLLVMProfileData -lLLVMObject -lLLVMTextAPI -lLLVMBitReader -lLLVMCore -lLLVMRemarks -lLLVMBitstreamReader -lLLVMAArch64AsmParser -lLLVMMCParser -lLLVMAArch64Desc -lLLVMMC -lLLVMDebugInfoCodeView -lLLVMDebugInfoMSF -lLLVMBinaryFormat -lLLVMAArch64Utils -lLLVMDemangle  -lLLVMAArch64Info  -lLLVMSupport -ltinfo
pluto_LDADD =  \
   ../piplib/libpiplib64.la \
   ../openscop/libosl.la \
   ../clan/libclan.la \
   ../cloog-isl/libcloog-isl.la \
   $(ISL_LIBADD) \
   ../polylib/libpolylib64.la \
   ../candl/libcandl.la \
   -lm

lib_LTLIBRARIES = libpluto.la 

# libpluto doesn't use polylib-based functions
libpluto_la_SOURCES = constraints.c constraints_isl.c math_support.c ddg.c transforms.c pluto.c post_transform.c framework.c polyloop.c iss.c libpluto.c libpluto_dummy.c constraints.h math_support.h pluto.h program.c program.h tile.c
libpluto_la_CPPFLAGS = $(OPT_FLAGS) $(DEBUG_FLAGS) \
   -DLIB_PLUTO -DSCOPLIB_INT_T_IS_LONGLONG -DCLOOG_INT_GMP \
   -I../include \
   -I../piplib/include \
   -I../clan/include \
   -I../openscop/include \
   -I../candl/include \
   -I../cloog-isl/include \
   $(ISL_INCLUDE)

# libpluto doesn't use polylib
libpluto_la_LIBADD = \
   ../piplib/libpiplib64.la \
   ../openscop/libosl.la \
   ../clan/libclan.la \
   ../candl/libcandl.la \
   $(ISL_LIBADD) \
   -lm -lgomp
