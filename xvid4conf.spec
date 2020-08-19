Summary: Tool to create XviD configuration files
Name:    xvid4conf
Version: 1.12
Release: 18%{?dist}
License: GPLv2+
URL:     http://www.exit1.org/archive/dvdrip-users/2005-07/msg00007.html
Source0: http://nexus.tfh-berlin.de/~t2/source/2.1/x/xvid4conf-%{version}.tar.bz2
Source1: xvid4conf.png

BuildRequires: gcc
BuildRequires: gtk2-devel
BuildRequires: desktop-file-utils

%description
This tool creates XviD configuration files. The generated configuration file
is meant to be read by transcode's xvid4 export module. This module (and so
the configuration file) is intended to be used with at least XviD 1.0.


%prep
%setup -q


%build
%configure
%make_build


%install
%make_install

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

# Install the desktop file
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    xvid4conf.desktop

# Icon for the desktop file
%{__install} -D -p -m 0644 %{SOURCE1} \
    %{buildroot}%{_datadir}/pixmaps/xvid4conf.png


%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/xvid4conf
%{_datadir}/applications/*xvid4conf.desktop
%{_datadir}/pixmaps/xvid4conf.png


%changelog
* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.12-14
- Remove Group tag
- Use make macros
- Add BuildRequires gcc
- Clean up spec file

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.12-13
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

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

