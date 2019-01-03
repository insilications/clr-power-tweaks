#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-power-tweaks
Version  : 180
Release  : 119
URL      : http://localhost/cgit/projects/clr-power-tweaks/snapshot/clr-power-tweaks-180.tar.xz
Source0  : http://localhost/cgit/projects/clr-power-tweaks/snapshot/clr-power-tweaks-180.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: clr-power-tweaks-autostart = %{version}-%{release}
Requires: clr-power-tweaks-bin = %{version}-%{release}
Requires: clr-power-tweaks-license = %{version}-%{release}
Requires: clr-power-tweaks-services = %{version}-%{release}
BuildRequires : autoconf
BuildRequires : automake-dev
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkgconfig(systemd)

%description
No detailed description available

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


%package services
Summary: services components for the clr-power-tweaks package.
Group: Systemd services

%description services
services components for the clr-power-tweaks package.


%prep
%setup -q -n clr-power-tweaks-180

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1546553713
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1546553713
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clr-power-tweaks
cp COPYING %{buildroot}/usr/share/package-licenses/clr-power-tweaks/COPYING
%make_install
## install_append content
mkdir %{buildroot}/usr/lib/systemd/system/timers.target.wants
ln -s ../clr-power.timer %{buildroot}/usr/lib/systemd/system/timers.target.wants/clr-power.timer
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/timers.target.wants/clr-power.timer

%files bin
%defattr(-,root,root,-)
/usr/bin/clr_power

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clr-power-tweaks/COPYING

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/timers.target.wants/clr-power.timer
/usr/lib/systemd/system/clr-power.service
/usr/lib/systemd/system/clr-power.timer
