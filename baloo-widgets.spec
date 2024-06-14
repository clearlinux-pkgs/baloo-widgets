#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v12
# autospec commit: fbcebd0
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : baloo-widgets
Version  : 24.05.1
Release  : 82
URL      : https://download.kde.org/stable/release-service/24.05.1/src/baloo-widgets-24.05.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.05.1/src/baloo-widgets-24.05.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.05.1/src/baloo-widgets-24.05.1.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
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
BuildRequires : gnupg
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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n baloo-widgets-24.05.1
cd %{_builddir}/baloo-widgets-24.05.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1718395439
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1718395439
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
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang baloowidgets5
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/baloo_filemetadata_temp_extractor
/usr/bin/baloo_filemetadata_temp_extractor

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/baloo-widgets.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/BalooWidgets/Baloo/FileMetaDataConfigWidget
/usr/include/KF6/BalooWidgets/Baloo/FileMetaDataWidget
/usr/include/KF6/BalooWidgets/Baloo/TagWidget
/usr/include/KF6/BalooWidgets/baloo/filemetadataconfigwidget.h
/usr/include/KF6/BalooWidgets/baloo/filemetadatawidget.h
/usr/include/KF6/BalooWidgets/baloo/tagwidget.h
/usr/include/KF6/BalooWidgets/baloo/widgets_export.h
/usr/lib64/cmake/KF6BalooWidgets/KF6BalooWidgetsConfig.cmake
/usr/lib64/cmake/KF6BalooWidgets/KF6BalooWidgetsConfigVersion.cmake
/usr/lib64/cmake/KF6BalooWidgets/KF6BalooWidgetsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6BalooWidgets/KF6BalooWidgetsTargets.cmake
/usr/lib64/libKF6BalooWidgets.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6BalooWidgets.so.24.05.1
/V3/usr/lib64/qt6/plugins/kf6/kfileitemaction/tagsfileitemaction.so
/V3/usr/lib64/qt6/plugins/kf6/propertiesdialog/baloofilepropertiesplugin.so
/usr/lib64/libKF6BalooWidgets.so.24.05.1
/usr/lib64/libKF6BalooWidgets.so.6
/usr/lib64/qt6/plugins/kf6/kfileitemaction/tagsfileitemaction.so
/usr/lib64/qt6/plugins/kf6/propertiesdialog/baloofilepropertiesplugin.so

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

