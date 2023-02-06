#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : baloo-widgets
Version  : 22.12.2
Release  : 61
URL      : https://download.kde.org/stable/release-service/22.12.2/src/baloo-widgets-22.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.12.2/src/baloo-widgets-22.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.12.2/src/baloo-widgets-22.12.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n baloo-widgets-22.12.2
cd %{_builddir}/baloo-widgets-22.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1675645302
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1675645302
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/baloo-widgets
cp %{_builddir}/baloo-widgets-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/baloo-widgets/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/baloo-widgets-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/baloo-widgets/2123756e0b1fc8243547235a33c0fcabfe3b9a51 || :
cp %{_builddir}/baloo-widgets-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/baloo-widgets/a4c60b3fefda228cd7439d3565df043192fef137 || :
cp %{_builddir}/baloo-widgets-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/baloo-widgets/a4c60b3fefda228cd7439d3565df043192fef137 || :
cp %{_builddir}/baloo-widgets-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/baloo-widgets/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567 || :
cp %{_builddir}/baloo-widgets-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/baloo-widgets/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567 || :
cp %{_builddir}/baloo-widgets-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/baloo-widgets/19d98e1b6f8ef12849ea4012a052d3907f336c91 || :
cp %{_builddir}/baloo-widgets-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/baloo-widgets/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/baloo-widgets-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/baloo-widgets/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/baloo-widgets-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/baloo-widgets/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/baloo-widgets-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/baloo-widgets/e458941548e0864907e654fa2e192844ae90fc32 || :
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
/usr/lib64/libKF5BalooWidgets.so.22.12.2
/usr/lib64/libKF5BalooWidgets.so.5
/usr/lib64/qt5/plugins/kf5/kfileitemaction/tagsfileitemaction.so
/usr/lib64/qt5/plugins/kf5/propertiesdialog/baloofilepropertiesplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/baloo-widgets/19d98e1b6f8ef12849ea4012a052d3907f336c91
/usr/share/package-licenses/baloo-widgets/2123756e0b1fc8243547235a33c0fcabfe3b9a51
/usr/share/package-licenses/baloo-widgets/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/baloo-widgets/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/baloo-widgets/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/baloo-widgets/a4c60b3fefda228cd7439d3565df043192fef137
/usr/share/package-licenses/baloo-widgets/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f baloowidgets5.lang
%defattr(-,root,root,-)

