import opensees.openseespy as ops

pid = ops.getPID()
np = ops.getNP()

print('Hello World Process:', pid)
if pid == 0:
    print('Total number of processes:', np)

