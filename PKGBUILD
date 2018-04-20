# Script generated with Bloom
pkgdesc="ROS - Contains transforms (e.g. differential drive inverse kinematics) for the various types of mobile robot platforms."
url='http://wiki.ros.org/ecl_mobile_robot'

pkgname='ros-kinetic-ecl-mobile-robot'
pkgver='0.60.3_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-ecl-build'
'ros-kinetic-ecl-errors'
'ros-kinetic-ecl-formatters'
'ros-kinetic-ecl-geometry'
'ros-kinetic-ecl-license'
'ros-kinetic-ecl-linear-algebra'
'ros-kinetic-ecl-math'
)

depends=('ros-kinetic-ecl-build'
'ros-kinetic-ecl-errors'
'ros-kinetic-ecl-formatters'
'ros-kinetic-ecl-geometry'
'ros-kinetic-ecl-license'
'ros-kinetic-ecl-linear-algebra'
'ros-kinetic-ecl-math'
)

conflicts=()
replaces=()

_dir=ecl_mobile_robot
source=()
md5sums=()

prepare() {
    cp -R $startdir/ecl_mobile_robot $srcdir/ecl_mobile_robot
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

