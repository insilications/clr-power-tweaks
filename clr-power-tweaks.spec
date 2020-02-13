#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-power-tweaks
Version  : 206
Release  : 134
URL      : https://github.com/clearlinux/clr-power-tweaks/archive/206/clr-power-tweaks-206.tar.gz
Source0  : https://github.com/clearlinux/clr-power-tweaks/archive/206/clr-power-tweaks-206.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: clr-power-tweaks-autostart = %{version}-%{release}
Requires: clr-power-tweaks-bin = %{version}-%{release}
Requires: clr-power-tweaks-license = %{version}-%{release}
Requires: clr-power-tweaks-man = %{version}-%{release}
Requires: clr-power-tweaks-services = %{version}-%{release}
BuildRequires : autoconf
BuildRequires : automake-dev
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkgconfig(systemd)

%description
# clr-power-tweaks
This is a utility, authored for the purposes of Clear Linux, that sets
reasonable power management defaults for platform devices. This is to improve
energy efficiency while platform is idle.

%package autostart
Summary: autostart components for the clr-power-tweaks package.
Group: Default

%description autostart
autostart components for the clr-power-tweaks package.


%package bin
Summary: bin components for the clr-power-tweaks package.
Group: Binaries
Requires: clr-power-tweaks-license = %{version}-%{release}
Requires: clr-power-tweaks-services = %{version}-%{release}

%description bin
bin components for the clr-power-tweaks package.


%package license
Summary: license components for the clr-power-tweaks package.
Group: Default

%description license
license components for the clr-power-tweaks package.


%package man
Summary: man components for the clr-power-tweaks package.
Group: Default

%description man
man components for the clr-power-tweaks package.


%package services
Summary: services components for the clr-power-tweaks package.
Group: Systemd services

%description services
services components for the clr-power-tweaks package.


%prep
%setup -q -n clr-power-tweaks-206
cd %{_builddir}/clr-power-tweaks-206

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581618999
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1581618999
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clr-power-tweaks
cp %{_builddir}/clr-power-tweaks-206/COPYING %{buildroot}/usr/share/package-licenses/clr-power-tweaks/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install
## install_append content
mkdir %{buildroot}/usr/lib/systemd/system/timers.target.wants
ln -s ../clr-power.timer %{buildroot}/usr/lib/systemd/system/timers.target.wants/clr-power.timer
mkdir %{buildroot}/usr/lib/systemd/system/sysinit.target.wants
ln -s ../clr-power-rfkill.service %{buildroot}/usr/lib/systemd/system/sysinit.target.wants/clr-power-rfkill.service
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/sysinit.target.wants/clr-power-rfkill.service
/usr/lib/systemd/system/timers.target.wants/clr-power.timer

%files bin
%defattr(-,root,root,-)
/usr/bin/clr_power

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clr-power-tweaks/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/clr_power.1
/usr/share/man/man5/clr-power-tweaks.conf.5

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/sysinit.target.wants/clr-power-rfkill.service
%exclude /usr/lib/systemd/system/timers.target.wants/clr-power.timer
/usr/lib/systemd/system/clr-power-rfkill.service
/usr/lib/systemd/system/clr-power.service
/usr/lib/systemd/system/clr-power.timer
