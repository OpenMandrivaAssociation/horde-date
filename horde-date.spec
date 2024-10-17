%define prj Horde_Date

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-date
Version:       0.1.0
Release:       4
Summary:       Horde Date package
License:       LGPL
Group:         Networking/Mail
Url:           https://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): php-pear
Requires:      horde-framework
Requires:      php-pear
Requires:      php-pear-Date
Requires:      php-pear-channel-horde
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde


%description
Package for creating and manipulating dates.

%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde/Date
%{peardir}/Horde/Date.php
%{peardir}/Horde/Date/Recurrence.php
%dir %{peardir}/tests/Horde_Date
%dir %{peardir}/tests/Horde_Date/tests
%dir %{peardir}/tests/Horde_Date/tests/fixtures
%{peardir}/tests/Horde_Date/tests/*.phpt
%{peardir}/tests/Horde_Date/tests/fixtures/bug2813.ics



%changelog
* Mon Jul 26 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.1.0-3mdv2011.0
+ Revision: 560542
- Increased release for rebuild

* Thu Mar 18 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.1.0-2mdv2010.1
+ Revision: 524826
- replaced Requires(pre): %%{_bindir}/pear with Requires(pre): php-pear
  increased rel version

* Sat Feb 27 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.1.0-1mdv2010.1
+ Revision: 512358
- removed BuildRequires: horde-framework
- replaced PreRq with Requires(pre)
- Initial import

