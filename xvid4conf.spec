Summary: Tool to create XviD configuration files
Name: xvid4conf
Version: 1.12
Release: 11%{?dist}
License: GPLv2+
Group: Applications/Multimedia
URL: http://www.exit1.org/archive/dvdrip-users/2005-07/msg00007.html
Source0: http://nexus.tfh-berlin.de/~t2/source/2.1/x/xvid4conf-%{version}.tar.bz2
Source1: xvid4conf.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk2-devel, desktop-file-utils

%description
This tool creates XviD configuration files. The generated configuration file
is meant to be read by transcode's xvid4 export module. This module (and so
the configuration file) is intended to be used with at least XviD 1.0.


%prep
%setup
# Create the desktop file
%{__cat} > xvid4conf.desktop << EOF
[Desktop Entry]
Name=XviD Configurator
Comment=Create XviD configuration files to use with transcode and dvd::rip
Exec=xvid4conf
Icon=xvid4conf
Terminal=false
Type=Application
Categories=Application;AudioVideo;
EOF


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall

# Install the desktop file
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    xvid4conf.desktop

# Icon for the desktop file
%{__install} -D -p -m 0644 %{SOURCE1} \
    %{buildroot}%{_datadir}/pixmaps/xvid4conf.png


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/xvid4conf
%{_datadir}/applications/*xvid4conf.desktop
%{_datadir}/pixmaps/xvid4conf.png


%changelog
* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Mar 20 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.12-7
- Mass rebuilt for Fedora 19 Features

* Wed Jan 25 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.12-4
- rebuild for new F11 features

* Sat Oct 18 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 1.12-3
- rebuild for RPM Fusion

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 1.12-2
- Release bump to drop the disttag number in FC5 build.

* Mon Jan  9 2006 Matthias Saou <http://freshrpms.net/> 1.12-1
- Initial RPM release.

