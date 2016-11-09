Name:           ros-indigo-ecl-navigation
Version:        0.60.3
Release:        0%{?dist}
Summary:        ROS ecl_navigation package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/ecl_navigation
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-ecl-mobile-robot
BuildRequires:  ros-indigo-catkin

%description
This stack aims to bring the common tools and algorithms needed to develop
navigation algorithms, in particular slam. It does not focus on the end-point
solution, rather the tools needed to create a variety of end-point solutions.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Nov 09 2016 Daniel Stonier <d.stonier@gmail.com> - 0.60.3-0
- Autogenerated by Bloom

* Wed Jan 06 2016 Daniel Stonier <d.stonier@gmail.com> - 0.60.1-1
- Autogenerated by Bloom

* Tue Nov 24 2015 Daniel Stonier <d.stonier@gmail.com> - 0.60.1-0
- Autogenerated by Bloom

