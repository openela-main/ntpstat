Name:		ntpstat
Version:	0.5
Release:	2%{?dist}
Summary:	Utility to print NTP synchronization status

License:	MIT
URL:		https://github.com/mlichvar/ntpstat
Source0:	https://github.com/mlichvar/ntpstat/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch

Requires:	chrony
# ntpstat was split off from the ntp package
Conflicts:	ntp < 4.2.8p10-4

%description
This package contains a script which prints a brief summary of the system
clock's synchronisation status when the ntpd or chronyd daemon is running.

%prep
%setup -q

%build

%install
make install bindir=$RPM_BUILD_ROOT%{_bindir} mandir=$RPM_BUILD_ROOT%{_mandir}

%files
%license COPYING
%doc NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Apr 17 2018 Miroslav Lichvar <mlichvar@redhat.com> 0.5-2
- don't require ntp in boolean dependency (#1561527)

* Tue Mar 20 2018 Miroslav Lichvar <mlichvar@redhat.com> 0.5-1
- update to 0.5

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 04 2017 Miroslav Lichvar <mlichvar@redhat.com> 0.4-3
- fix more issues found in package review (#1510565)

* Thu Nov 23 2017 Miroslav Lichvar <mlichvar@redhat.com> 0.4-2
- fix issues found in package review (#1510565)

* Tue Nov 07 2017 Miroslav Lichvar <mlichvar@redhat.com> 0.4-1
- update to 0.4
- split ntpstat off from ntp package
