#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-power-tweaks
Version  : 165
Release  : 103
URL      : http://localhost/cgit/projects/clr-power-tweaks/snapshot/clr-power-tweaks-165.tar.gz
Source0  : http://localhost/cgit/projects/clr-power-tweaks/snapshot/clr-power-tweaks-165.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: clr-power-tweaks-bin
Requires: clr-power-tweaks-config
Requires: clr-power-tweaks-autostart
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
Requires: clr-power-tweaks-config

%description bin
bin components for the clr-power-tweaks package.


%package config
Summary: config components for the clr-power-tweaks package.
Group: Default

%description config
config components for the clr-power-tweaks package.


%prep
%setup -q -n clr-power-tweaks-165

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1513985530
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1513985530
rm -rf %{buildroot}
%make_install
## make_install_append content
mkdir %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -s ../clr-power.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/clr-power.service
## make_install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/clr-power.service

%files bin
%defattr(-,root,root,-)
/usr/bin/clr_power

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/clr-power.service
/usr/lib/systemd/system/clr-power.service
/usr/lib/tmpfiles.d/clr-power-tweaks.conf
