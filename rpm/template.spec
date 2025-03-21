%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-robot-localization
Version:        3.9.2
Release:        2%{?dist}%{?release_suffix}
Summary:        ROS robot_localization package

License:        Apache License 2.0
URL:            http://ros.org/wiki/robot_localization
Source0:        %{name}-%{version}.tar.gz

Requires:       GeographicLib-devel
Requires:       boost-devel
Requires:       eigen3-devel
Requires:       ros-rolling-angles
Requires:       ros-rolling-builtin-interfaces
Requires:       ros-rolling-diagnostic-msgs
Requires:       ros-rolling-diagnostic-updater
Requires:       ros-rolling-geographic-msgs
Requires:       ros-rolling-geometry-msgs
Requires:       ros-rolling-message-filters
Requires:       ros-rolling-nav-msgs
Requires:       ros-rolling-rclcpp
Requires:       ros-rolling-rosidl-default-runtime
Requires:       ros-rolling-sensor-msgs
Requires:       ros-rolling-std-msgs
Requires:       ros-rolling-std-srvs
Requires:       ros-rolling-tf2
Requires:       ros-rolling-tf2-eigen
Requires:       ros-rolling-tf2-geometry-msgs
Requires:       ros-rolling-tf2-ros
Requires:       ros-rolling-yaml-cpp-vendor
Requires:       ros-rolling-ros-workspace
BuildRequires:  GeographicLib-devel
BuildRequires:  boost-devel
BuildRequires:  eigen3-devel
BuildRequires:  ros-rolling-ament-cmake
BuildRequires:  ros-rolling-angles
BuildRequires:  ros-rolling-builtin-interfaces
BuildRequires:  ros-rolling-diagnostic-msgs
BuildRequires:  ros-rolling-diagnostic-updater
BuildRequires:  ros-rolling-geographic-msgs
BuildRequires:  ros-rolling-geometry-msgs
BuildRequires:  ros-rolling-message-filters
BuildRequires:  ros-rolling-nav-msgs
BuildRequires:  ros-rolling-rclcpp
BuildRequires:  ros-rolling-rosidl-default-generators
BuildRequires:  ros-rolling-sensor-msgs
BuildRequires:  ros-rolling-std-msgs
BuildRequires:  ros-rolling-std-srvs
BuildRequires:  ros-rolling-tf2
BuildRequires:  ros-rolling-tf2-eigen
BuildRequires:  ros-rolling-tf2-geometry-msgs
BuildRequires:  ros-rolling-tf2-ros
BuildRequires:  ros-rolling-yaml-cpp-vendor
BuildRequires:  ros-rolling-ros-workspace
BuildRequires:  ros-rolling-rosidl-typesupport-fastrtps-c
BuildRequires:  ros-rolling-rosidl-typesupport-fastrtps-cpp
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}
Provides:       ros-rolling-rosidl-interface-packages(member)

%if 0%{?with_tests}
BuildRequires:  ros-rolling-ament-cmake-gtest
BuildRequires:  ros-rolling-ament-lint-auto
BuildRequires:  ros-rolling-ament-lint-common
BuildRequires:  ros-rolling-launch-ros
BuildRequires:  ros-rolling-launch-testing-ament-cmake
%endif

%if 0%{?with_weak_deps}
Supplements:    ros-rolling-rosidl-interface-packages(all)
%endif

%description
Provides nonlinear state estimation through sensor fusion of an abritrary number
of sensors.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Fri Mar 21 2025 Tom Moore <ayrton04@gmail.com> - 3.9.2-2
- Autogenerated by Bloom

* Fri Mar 21 2025 Tom Moore <ayrton04@gmail.com> - 3.9.2-1
- Autogenerated by Bloom

* Thu Aug 29 2024 Tom Moore <ayrton04@gmail.com> - 3.9.1-1
- Autogenerated by Bloom

* Wed Apr 24 2024 Tom Moore <ayrton04@gmail.com> - 3.9.0-1
- Autogenerated by Bloom

* Sun Apr 21 2024 Tom Moore <ayrton04@gmail.com> - 3.8.0-1
- Autogenerated by Bloom

* Tue Apr 16 2024 Tom Moore <ayrton04@gmail.com> - 3.6.1-1
- Autogenerated by Bloom

* Tue Mar 19 2024 Tom Moore <ayrton04@gmail.com> - 3.6.0-3
- Autogenerated by Bloom

* Wed Mar 06 2024 Tom Moore <ayrton04@gmail.com> - 3.6.0-2
- Autogenerated by Bloom

