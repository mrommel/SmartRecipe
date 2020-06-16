#!/bin/sh
#
#
python_pidfile=./python.pid

if [ -f $python_pidfile ]
then
	python_pid=`cat $python_pidfile`
fi

# Start the service node
start() {
		echo "Starting python server: "
		
		if [ -f $python_pidfile ] ; then
				if test `ps -e | grep -c $python_pid` = 2; then
						echo "Not starting python - instance already running with PID: $python_pid"
				else
						echo "Starting python"
						python3 manage.py runserver 0.0.0.0:8023 &> ./python.log &
						echo $! > $python_pidfile
						sleep 5
				fi
		else
				echo "Starting python"
				python3 manage.py runserver 0.0.0.0:8023 &> ./python.log &
				echo $! > $python_pidfile
				sleep 5
		fi
		
        echo "node/python servers startup"
        echo
}
# Restart the service node
stop() {
        echo "Stopping python server: "
		
		if [ -f $python_pidfile ] ; then
				echo "stopping python"
				pkill -TERM -P $python_pid
				
				#killall python
		else
				echo "Cannot stop python - no Pidfile found!"
		fi
		
		echo "python server stopped"
        echo
}
status() {	
		
		if [ -f $python_pidfile ] ; then
				if test `ps -e | grep -c $python_pid` = 1; then
						echo "python not running"
				else
						echo "python running with PID: [$python_pid]"
				fi
		else
				echo "$python_pidfile does not exist! Cannot process python status!"
		fi
}

### main logic ###
case "$1" in
  start)
        start
        ;;
  stop)
        stop
        ;;
  status)
        status
        ;;
  restart|reload|condrestart)
        stop
        sleep 5
        start
        ;;
  *)
        echo $"Usage: $0 {start|stop|restart|reload|status}"
        exit 1
esac
exit 0