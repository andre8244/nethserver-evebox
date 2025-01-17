Summary: NethServer configuration for EveBox
Name: nethserver-evebox
Version: 1.4.0
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: nethserver-suricata
Requires: evebox >= 0.11.0
Requires: geolite2-city
Requires: nethserver-httpd-admin-service

BuildRequires: nethserver-devtools 

%description
NethServer configuration for EveBox

%prep
%setup

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist
echo "%doc COPYING" >> %{name}-%{version}-filelist
mkdir -p %{buildroot}/var/lib/evebox

%post

%preun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%dir %attr(0755, suricata, suricata) /var/lib/evebox

%changelog
* Wed Nov 25 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.4.0-1
- Access web applications from port 980 - NethServer/dev#6344

* Wed Nov 18 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.3.0-1
- New NethServer 7.9.2009 defaults - NethServer/dev#6320

* Wed Apr 01 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.2-1
- Evebox: update to 0.11.0 - NethServer/dev#6101

* Tue Feb 11 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.1-1
- Remove dynamic geolite support (#5)

* Tue Jun 11 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.0-1
- IPS Cockpit UI - NethServer/dev#5756

* Mon Dec 03 2018 Davide Principi <davide.principi@nethesis.it> - 1.1.0-1
- Evebox: add event history retention - NethServer/dev#5626

* Mon Aug 06 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1
- Storage Location of  GeoLite2-City.mmdb.gz - NethServer/dev#5559

* Mon Apr 30 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- Evebox: update to release 0.9.0 - NethServer/dev#5472

* Fri Oct 06 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- EveBox NethServer/dev#5346

