%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

%global __cmake_in_source_build 1

Name:           ros-humble-robot-localization
Version:        3.5.4
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS robot_localization package

License:        Apache License 2.0
URL:            http://ros.org/wiki/robot_localization
Source0:        %{name}-%{version}.tar.gz

Requires:       GeographicLib-devel
Requires:       boost-devel
Requires:       eigen3-devel
Requires:       ros-humble-angles
Requires:       ros-humble-diagnostic-msgs
Requires:       ros-humble-diagnostic-updater
Requires:       ros-humble-geographic-msgs
Requires:       ros-humble-geometry-msgs
Requires:       ros-humble-message-filters
Requires:       ros-humble-nav-msgs
Requires:       ros-humble-rclcpp
Requires:       ros-humble-rmw-implementation
Requires:       ros-humble-rosidl-default-runtime
Requires:       ros-humble-sensor-msgs
Requires:       ros-humble-std-msgs
Requires:       ros-humble-std-srvs
Requires:       ros-humble-tf2
Requires:       ros-humble-tf2-eigen
Requires:       ros-humble-tf2-geometry-msgs
Requires:       ros-humble-tf2-ros
Requires:       ros-humble-yaml-cpp-vendor
Requires:       ros-humble-ros-workspace
BuildRequires:  GeographicLib-devel
BuildRequires:  boost-devel
BuildRequires:  eigen3-devel
BuildRequires:  ros-humble-ament-cmake
BuildRequires:  ros-humble-angles
BuildRequires:  ros-humble-builtin-interfaces
BuildRequires:  ros-humble-diagnostic-msgs
BuildRequires:  ros-humble-diagnostic-updater
BuildRequires:  ros-humble-geographic-msgs
BuildRequires:  ros-humble-geometry-msgs
BuildRequires:  ros-humble-message-filters
BuildRequires:  ros-humble-nav-msgs
BuildRequires:  ros-humble-rclcpp
BuildRequires:  ros-humble-rmw-implementation
BuildRequires:  ros-humble-rosidl-default-generators
BuildRequires:  ros-humble-sensor-msgs
BuildRequires:  ros-humble-std-msgs
BuildRequires:  ros-humble-std-srvs
BuildRequires:  ros-humble-tf2
BuildRequires:  ros-humble-tf2-eigen
BuildRequires:  ros-humble-tf2-geometry-msgs
BuildRequires:  ros-humble-tf2-ros
BuildRequires:  ros-humble-yaml-cpp-vendor
BuildRequires:  ros-humble-ros-workspace
BuildRequires:  ros-humble-rosidl-typesupport-fastrtps-c
BuildRequires:  ros-humble-rosidl-typesupport-fastrtps-cpp
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}
Provides:       ros-humble-rosidl-interface-packages(member)

%if 0%{?with_tests}
BuildRequires:  ros-humble-ament-cmake-gtest
BuildRequires:  ros-humble-ament-lint-auto
BuildRequires:  ros-humble-ament-lint-common
BuildRequires:  ros-humble-launch-ros
BuildRequires:  ros-humble-launch-testing-ament-cmake
%endif

%if 0%{?with_weak_deps}
Supplements:    ros-humble-rosidl-interface-packages(all)
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
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
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
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Fri Aug 29 2025 Tom Moore <ayrton04@gmail.com> - 3.5.4-1
- Autogenerated by Bloom

* Tue Apr 16 2024 Tom Moore <ayrton04@gmail.com> - 3.5.3-1
- Autogenerated by Bloom

* Wed Dec 20 2023 Tom Moore <ayrton04@gmail.com> - 3.5.2-1
- Autogenerated by Bloom

* Wed May 24 2023 Tom Moore <ayrton04@gmail.com> - 3.5.1-2
- Autogenerated by Bloom

* Wed May 24 2023 Tom Moore <ayrton04@gmail.com> - 3.5.1-1
- Autogenerated by Bloom

* Wed May 17 2023 Tom Moore <ayrton04@gmail.com> - 3.4.2-1
- Autogenerated by Bloom

* Mon Apr 17 2023 Tom Moore <ayrton04@gmail.com> - 3.5.0-1
- Autogenerated by Bloom

* Tue Apr 19 2022 Tom Moore <ayrton04@gmail.com> - 3.3.1-2
- Autogenerated by Bloom

* Wed Mar 02 2022 Tom Moore <ayrton04@gmail.com> - 3.3.1-1
- Autogenerated by Bloom

* Tue Feb 08 2022 Tom Moore <ayrton04@gmail.com> - 3.3.0-2
- Autogenerated by Bloom

