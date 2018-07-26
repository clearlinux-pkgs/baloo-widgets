#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : baloo-widgets
Version  : 18.07.80
Release  : 4
URL      : https://github.com/KDE/baloo-widgets/archive/v18.07.80.tar.gz
Source0  : https://github.com/KDE/baloo-widgets/archive/v18.07.80.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: baloo-widgets-bin
Requires: baloo-widgets-lib
Requires: baloo-widgets-license
Requires: baloo-widgets-data
BuildRequires : baloo-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kcodecs-dev
BuildRequires : kcompletion-dev
BuildRequires : kfilemetadata-dev
BuildRequires : kio-dev
BuildRequires : kitemviews-dev
BuildRequires : kjobwidgets-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kxmlgui-dev
BuildRequires : solid-dev

%description
No detailed description available

%package bin
Summary: bin components for the baloo-widgets package.
Group: Binaries
Requires: baloo-widgets-data
Requires: baloo-widgets-license

%description bin
bin components for the baloo-widgets package.


%package data
Summary: data components for the baloo-widgets package.
Group: Data

%description data
data components for the baloo-widgets package.


%package dev
Summary: dev components for the baloo-widgets package.
Group: Development
Requires: baloo-widgets-lib
Requires: baloo-widgets-bin
Requires: baloo-widgets-data
Provides: baloo-widgets-devel

%description dev
dev components for the baloo-widgets package.


%package lib
Summary: lib components for the baloo-widgets package.
Group: Libraries
Requires: baloo-widgets-data
Requires: baloo-widgets-license

%description lib
lib components for the baloo-widgets package.


%package license
Summary: license components for the baloo-widgets package.
Group: Default

%description license
license components for the baloo-widgets package.


%prep
%setup -q -n baloo-widgets-18.07.80

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532646971
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1532646971
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/baloo-widgets
cp COPYING.README %{buildroot}/usr/share/doc/baloo-widgets/COPYING.README
cp COPYING.LIB %{buildroot}/usr/share/doc/baloo-widgets/COPYING.LIB
cp COPYING %{buildroot}/usr/share/doc/baloo-widgets/COPYING
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/baloo_filemetadata_temp_extractor

%files data
%defattr(-,root,root,-)
/usr/share/kservices5/baloofilepropertiesplugin.desktop

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/BalooWidgets/Baloo/FileMetaDataConfigWidget
/usr/include/KF5/BalooWidgets/Baloo/FileMetaDataWidget
/usr/include/KF5/BalooWidgets/Baloo/TagWidget
/usr/include/KF5/BalooWidgets/baloo/filemetadataconfigwidget.h
/usr/include/KF5/BalooWidgets/baloo/filemetadatawidget.h
/usr/include/KF5/BalooWidgets/baloo/tagwidget.h
/usr/include/KF5/BalooWidgets/baloo/widgets_export.h
/usr/lib64/cmake/KF5BalooWidgets/KF5BalooWidgetsConfig.cmake
/usr/lib64/cmake/KF5BalooWidgets/KF5BalooWidgetsConfigVersion.cmake
/usr/lib64/cmake/KF5BalooWidgets/KF5BalooWidgetsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5BalooWidgets/KF5BalooWidgetsTargets.cmake
/usr/lib64/libKF5BalooWidgets.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5BalooWidgets.so.18
/usr/lib64/libKF5BalooWidgets.so.18.7.80
/usr/lib64/qt5/plugins/baloofilepropertiesplugin.so

%files license
%defattr(-,root,root,-)
/usr/share/doc/baloo-widgets/COPYING
/usr/share/doc/baloo-widgets/COPYING.LIB
/usr/share/doc/baloo-widgets/COPYING.README
