import os
import argparse
import datetime
import subprocess

# example usage
# python3 script_mlir.py --config=onnx --reps=3 --data_sizes=5,50,3 --out_prefix=timesheet

# This outputs in timesheet-onnx.csv
# First column is data size, rest are time readings for each repetition

parser = argparse.ArgumentParser()
parser.add_argument(
    "--config",
    type=str,
    choices=["pipe-json", "pipe-bytes", "onnx", "tf", "grpc"],              # protobuf not yet supported
    help="Method for communication",
    default="onnx"
)
# range of data sizes: start,end,step
parser.add_argument(
    "--data_sizes",
    type=str,
    help="Range of data sizes",
    default=1
)
parser.add_argument(
    "--pipe_name",
    type=str,
    help="Pipe name",
    default="mlir-hello"
)
parser.add_argument(
    "--reps",
    type=int,
    help="Number of repetitions",
    default=1
)
parser.add_argument(
    "--out_prefix",
    type=str,
    help="Prefix to output file name",
    default="timesheet"
)

args = parser.parse_args()

# base_cmd = ' echo 5 10 '

# ################ FOR MLIR ##################
# REPO_DIR = '/home/cs20btech11024/repos/ml-llvm-project'
# BUILD_DIR = f'{REPO_DIR}/build_mlir_llvm10_release'
# base_cmd = f'{BUILD_DIR}/bin/mlir-opt -mlir-hello-mlbridge {REPO_DIR}/mlir/test/Target/llvmir.mlir -o test.log '
# commands = {
#     'onnx' : base_cmd + '-mlir-hello-use-onnx',
#     'pipe-json' : base_cmd + '--mlir-hello-use-pipe --mlir-hello-pipe-name=' + args.pipe_name + ' --mlir-hello-data-format=json',
#     'pipe-bytes' : base_cmd + '--mlir-hello-use-pipe --mlir-hello-pipe-name=' + args.pipe_name + ' --mlir-hello-data-format=bytes',
#     'tf' : base_cmd,
#     'grpc': base_cmd + ' --mlir-hello-server-address=0.0.0.0:5050'
# }   



############ FOR PLUTO ######################
REPO_DIR = '/home/cs20btech11024/repos/Pluto-MLBridge'
base_cmd = f'{REPO_DIR}/polycc examples/matmul/matmul.c  --silent'

n = [10, 20, 1]                         # default range for data_size
arg_n = args.data_sizes.split(',')
for i in range(len(arg_n)):
    n[i] = int(arg_n[i])
print(n)
input()
outfile = args.out_prefix + '-'+ args.config + '.csv'


with open(outfile, "a") as f:
    f.write('\n')
    f.write(str(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")) + '\n')  
    f.write(args.config+'\n')        # can  comment out header portion if not required

    for data_size in range(n[0], n[1], n[2]):
        f.write(str(data_size))
        for i in range(args.reps):
            
            # cmd = commands[args.config] + ' --mlir-hello-data-size=' + str(data_size)
            with open('tmp', 'w') as f2:
                f2.write(str(data_size))
            cmd = base_cmd + ' < tmp'
            print("Command:", cmd)
            os.system(cmd)
            # pro = subprocess.Popen(commands[args.config] + ' --hello-data-size=' + str(data_size), executable='/bin/bash', shell=True,
            #                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf8')
            # # Output_cmd2 = pro.stdout
            # (Output_cmd2, err) = pro.communicate()

            # # line = Output_cmd2.readline()
            # line = Output_cmd2
            # print("Output_cmd2", line)
            # if pro.stderr is not None:
            #     logging.critical('Error : {}'.format(pro.stderr))
            #     print('Error : {}'.format(pro.stderr))
            # if not line:
            #     print("Read line is:", line)
            # else:
            #     print("line not writen")
                
            
            
            # # res = os.popen(commands[args.config] + ' --hello-data-size=' + str(data_size)).read()
            # # print("Response:", res, type(res))
            # res = line.split(' ')
            # f.write(','+ res[1])
        f.write('\n')
    
print('Times written to', outfile)

# import os

# num_reps = 3
# pipename = 'mlir-pipe'

# base_cmd = '/home/cs20mtech12003/ml-llvm-project/build_mlir/bin/mlir-opt --helloworld /home/cs20mtech12003/ml-llvm-project/mlir/test/IR/affine-map.mlir -allow-unregistered-dialect '

# commands = {
#     'onnx' : base_cmd + '--hello-use-onnx',
#     'pipe-json' : base_cmd + '--hello-use-pipe --hello-pipe-name= ' + pipename + ' --hello-data-format=json',
#     'pipe-bytes' : base_cmd + '--hello-use-pipe --hello-pipe-name=pipename ' + pipename + ' --hello-data-format=bytes'
# }   

# for cmd in commands.keys():
#     for data_size in range(10,100,5):
#         for i in range(num_reps):
#             os.system(commands[cmd] + ' --hello-data-size=' + str(data_size))
