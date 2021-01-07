#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : baloo-widgets
Version  : 20.12.1
Release  : 39
URL      : https://download.kde.org/stable/release-service/20.12.1/src/baloo-widgets-20.12.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.12.1/src/baloo-widgets-20.12.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.12.1/src/baloo-widgets-20.12.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: baloo-widgets-bin = %{version}-%{release}
Requires: baloo-widgets-data = %{version}-%{release}
Requires: baloo-widgets-lib = %{version}-%{release}
Requires: baloo-widgets-license = %{version}-%{release}
Requires: baloo-widgets-locales = %{version}-%{release}
BuildRequires : baloo-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kfilemetadata-dev
BuildRequires : qtbase-dev mesa-dev

%description
No detailed description available

%package bin
Summary: bin components for the baloo-widgets package.
Group: Binaries
Requires: baloo-widgets-data = %{version}-%{release}
Requires: baloo-widgets-license = %{version}-%{release}

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
Requires: baloo-widgets-lib = %{version}-%{release}
Requires: baloo-widgets-bin = %{version}-%{release}
Requires: baloo-widgets-data = %{version}-%{release}
Provides: baloo-widgets-devel = %{version}-%{release}
Requires: baloo-widgets = %{version}-%{release}

%description dev
dev components for the baloo-widgets package.


%package lib
Summary: lib components for the baloo-widgets package.
Group: Libraries
Requires: baloo-widgets-data = %{version}-%{release}
Requires: baloo-widgets-license = %{version}-%{release}

%description lib
lib components for the baloo-widgets package.


%package license
Summary: license components for the baloo-widgets package.
Group: Default

%description license
license components for the baloo-widgets package.


%package locales
Summary: locales components for the baloo-widgets package.
Group: Default

%description locales
locales components for the baloo-widgets package.


%prep
%setup -q -n baloo-widgets-20.12.1
cd %{_builddir}/baloo-widgets-20.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610036993
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1610036993
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/baloo-widgets
cp %{_builddir}/baloo-widgets-20.12.1/COPYING %{buildroot}/usr/share/package-licenses/baloo-widgets/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/baloo-widgets-20.12.1/COPYING.LIB %{buildroot}/usr/share/package-licenses/baloo-widgets/01a6b4bf79aca9b556822601186afab86e8c4fbf
cp %{_builddir}/baloo-widgets-20.12.1/COPYING.README %{buildroot}/usr/share/package-licenses/baloo-widgets/6070c553a9e29baa98a1fb7ae983e8d7fa14b7d7
pushd clr-build
%make_install
popd
%find_lang baloowidgets5

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/baloo_filemetadata_temp_extractor

%files data
%defattr(-,root,root,-)
/usr/share/kservices5/baloofilepropertiesplugin.desktop
/usr/share/qlogging-categories5/baloo-widgets.categories

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
/usr/lib64/libKF5BalooWidgets.so.20.12.1
/usr/lib64/libKF5BalooWidgets.so.5
/usr/lib64/qt5/plugins/baloofilepropertiesplugin.so
/usr/lib64/qt5/plugins/kf5/kfileitemaction/tagsfileitemaction.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/baloo-widgets/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/baloo-widgets/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/baloo-widgets/6070c553a9e29baa98a1fb7ae983e8d7fa14b7d7

%files locales -f baloowidgets5.lang
%defattr(-,root,root,-)

