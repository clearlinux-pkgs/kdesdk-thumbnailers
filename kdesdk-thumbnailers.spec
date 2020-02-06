#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kdesdk-thumbnailers
Version  : 19.12.2
Release  : 17
URL      : https://download.kde.org/stable/release-service/19.12.2/src/kdesdk-thumbnailers-19.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.2/src/kdesdk-thumbnailers-19.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.2/src/kdesdk-thumbnailers-19.12.2.tar.xz.sig
Summary  : Plugins for the thumbnailing system
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: kdesdk-thumbnailers-data = %{version}-%{release}
Requires: kdesdk-thumbnailers-lib = %{version}-%{release}
Requires: kdesdk-thumbnailers-license = %{version}-%{release}
Requires: kdesdk-thumbnailers-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n kdesdk-thumbnailers-19.12.2
cd %{_builddir}/kdesdk-thumbnailers-19.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581019463
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1581019463
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdesdk-thumbnailers
cp %{_builddir}/kdesdk-thumbnailers-19.12.2/COPYING %{buildroot}/usr/share/package-licenses/kdesdk-thumbnailers/a21ac62aee75f8fcb26b1de6fc90e5eea271854c
cp %{_builddir}/kdesdk-thumbnailers-19.12.2/cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/kdesdk-thumbnailers/ff3ed70db4739b3c6747c7f624fe2bad70802987
pushd clr-build
%make_install
popd
%find_lang pothumbnail

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/config.kcfg/pocreatorsettings.kcfg
/usr/share/kservices5/pothumbnail.desktop

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/pothumbnail.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdesdk-thumbnailers/a21ac62aee75f8fcb26b1de6fc90e5eea271854c
/usr/share/package-licenses/kdesdk-thumbnailers/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files locales -f pothumbnail.lang
%defattr(-,root,root,-)

