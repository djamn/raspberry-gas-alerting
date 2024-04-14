#! /bin/sh

### BEGIN INIT INFO
# Provides:          check-air.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
### END INIT INFO

# CONFIG VALUES
LATEST_VERSION="1.0.0 (14/04/2024)"
FILE_NAME="Air-Quality-Check"
PATH_NAME=/usr/local/bin/check-air

echo "Latest Version: $LATEST_VERSION"

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting $FILE_NAME..."
    $PATH_NAME &
    ;;
  stop)
    echo "Stopping $FILE_NAME..."
    pkill -f $PATH_NAME
    ;;
  *)
    echo "Usage: /etc/init.d/air-quality.sh {start|stop}"
    exit 1
    ;;
esac

exit 0
