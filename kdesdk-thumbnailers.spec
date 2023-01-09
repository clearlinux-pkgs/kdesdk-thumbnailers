#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3A6A4DB839EAA6D7 (aacid@kde.org)
#
Name     : kdesdk-thumbnailers
Version  : 22.12.1
Release  : 48
URL      : https://download.kde.org/stable/release-service/22.12.1/src/kdesdk-thumbnailers-22.12.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.12.1/src/kdesdk-thumbnailers-22.12.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.12.1/src/kdesdk-thumbnailers-22.12.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-3.0
Requires: kdesdk-thumbnailers-data = %{version}-%{release}
Requires: kdesdk-thumbnailers-lib = %{version}-%{release}
Requires: kdesdk-thumbnailers-license = %{version}-%{release}
Requires: kdesdk-thumbnailers-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : qtbase-dev mesa-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package data
Summary: data components for the kdesdk-thumbnailers package.
Group: Data

%description data
data components for the kdesdk-thumbnailers package.


%package lib
Summary: lib components for the kdesdk-thumbnailers package.
Group: Libraries
Requires: kdesdk-thumbnailers-data = %{version}-%{release}
Requires: kdesdk-thumbnailers-license = %{version}-%{release}

%description lib
lib components for the kdesdk-thumbnailers package.


%package license
Summary: license components for the kdesdk-thumbnailers package.
Group: Default

%description license
license components for the kdesdk-thumbnailers package.


%package locales
Summary: locales components for the kdesdk-thumbnailers package.
Group: Default

%description locales
locales components for the kdesdk-thumbnailers package.


%prep
%setup -q -n kdesdk-thumbnailers-22.12.1
cd %{_builddir}/kdesdk-thumbnailers-22.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1673306977
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
export SOURCE_DATE_EPOCH=1673306977
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdesdk-thumbnailers
cp %{_builddir}/kdesdk-thumbnailers-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kdesdk-thumbnailers/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kdesdk-thumbnailers-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kdesdk-thumbnailers/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/kdesdk-thumbnailers-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kdesdk-thumbnailers/2123756e0b1fc8243547235a33c0fcabfe3b9a51 || :
cp %{_builddir}/kdesdk-thumbnailers-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kdesdk-thumbnailers/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kdesdk-thumbnailers-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kdesdk-thumbnailers/7d9831e05094ce723947d729c2a46a09d6e90275 || :
pushd clr-build
%make_install
popd
%find_lang pothumbnail

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/config.kcfg/pocreatorsettings.kcfg

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kf5/thumbcreator/pothumbnail.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdesdk-thumbnailers/2123756e0b1fc8243547235a33c0fcabfe3b9a51
/usr/share/package-licenses/kdesdk-thumbnailers/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kdesdk-thumbnailers/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kdesdk-thumbnailers/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f pothumbnail.lang
%defattr(-,root,root,-)

