#Imporditakse teeigd:
import vrep                  #V-rep's library
import sys
import time
      
vrep.simxFinish(-1) #It is closing all open connections with VREP
clientID=vrep.simxStart('127.0.0.1',19997,True,True,5000,5)
if clientID!=-1:  #It is checking if connection is successful
    print 'Connected to remote API server'   
else:
    print 'Connection not successful'
    sys.exit('Could not connect')

#Getting motor handles
errorCode,left_motor_handle=vrep.simxGetObjectHandle(clientID,"left_joint",vrep.simx_opmode_oneshot_wait)
errorCode,right_motor_handle=vrep.simxGetObjectHandle(clientID,"right_joint",vrep.simx_opmode_oneshot_wait)
sensor_h=[] #handles list
sensor_val=[] #Sensor value list

#Getting sensor handles list
for x in range(0,6):
        errorCode,sensor_handle=vrep.simxGetObjectHandle(clientID,'line_sensor'+str(x),vrep.simx_opmode_oneshot_wait)
        sensor_h.append(sensor_handle) #It is adding sensor handle values
        errorCode,detectionstate, sensorreadingvalue=vrep.simxReadVisionSensor(clientID,sensor_h[x],vrep.simx_opmode_streaming)
        sensor_val.append(1.0) #It is adding 1.0 to fill the sensor values on the list. In the while loop it is going to overwrite the values
time.sleep(1)
t = time.time() #It is saving the time which is now
while (1):  #Cycle which doesn't end
    #It is writing down sensor handles and reading values
    summa = 0  #It is zeroing the  sum 
    andur = 0	#and the sensor values 
    for x in range(0,6):
        errorCode,detectionstate, sensorreadingvalue=vrep.simxReadVisionSensor(clientID,sensor_h[x],vrep.simx_opmode_buffer)
        #Reading sensor values
        sensor_val[x]=sensorreadingvalue[1][0] #It is overwriting the sensor values
        print "Positsiooni väärtus kokku45 :",sensor_val[x] ,x
    if sensor_val[2]<=0.2 or sensor_val[3]<=0.2:
        errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,10, vrep.simx_opmode_streaming)
        errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,10, vrep.simx_opmode_streaming)
    if sensor_val[1]<=0.2: 
        errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,13, vrep.simx_opmode_streaming)
        errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,10, vrep.simx_opmode_streaming)
    if sensor_val[0]<=0.2: 
        errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,16, vrep.simx_opmode_streaming)
        errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,10, vrep.simx_opmode_streaming)  
    if sensor_val[4]<=0.2: 
        errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,10, vrep.simx_opmode_streaming)
        errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,13, vrep.simx_opmode_streaming)   
    if sensor_val[5]<=0.2: 
        errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,10, vrep.simx_opmode_streaming)
        errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,16, vrep.simx_opmode_streaming)     
    viivitus = round((time.time()-t),5) #calculating delay time
    print "viivitus on: ", viivitus
    t = time.time() #Taking new time moment





















