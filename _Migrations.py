import sys

def information():
    message = """
    Example :
    python filename.py --arguments
    
    arguments List :
    --reset \t reset migration
    --run \t continue migration from last migration, if last migration is None, argument running new migration
    --rollback \t rollback migration 1 step
    \t --n \t rollback migration n step, n is integer and n > 0
    """
    print(message)

argvLen = len(sys.argv)
if(argvLen <= 1):
    information()
elif(argvLen > 1 ):
    args1List = [
        '--reset',
        '--run',
        '--rollback'
        ]
    argv1 = sys.argv[1]
    
    if(argv1 not in args1List):
        information
    elif(argv1 == '--reset'):
        print('doing reset')
    elif(argv1 == '--run'):
        print('doing run')
    elif(argv1 == '--rollback'):
        if(argvLen > 2):
            argv2 = int((sys.argv[2]).replace('--',''))
            if(argv2 <= 0):
                information()
            else:
                print(f'doing {argv2} step')
        else:    
            print('doing 1 step')

    

