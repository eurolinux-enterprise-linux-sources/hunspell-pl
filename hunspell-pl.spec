Name: hunspell-pl
Summary: Polish hunspell dictionaries
%define upstreamid 20130130
Version: 0.%{upstreamid}
Release: 1%{?dist}
Source: http://sjp.pl/slownik/ort/sjp-myspell-pl-%{upstreamid}.zip
Group: Applications/Text
URL: http://www.kurnik.pl/dictionary/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+ or GPL+ or MPLv1.1 or CC-BY-SA
BuildArch: noarch

Requires: hunspell

%description
Polish hunspell dictionaries.

%prep
%setup -q -c hunspell-pl

%build
unzip pl_PL.zip

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_pl_PL.txt
%{_datadir}/myspell/*

%changelog
* Thu Jan 31 2013 Caolán McNamara <caolanm@redhat.com> - 0.20130130-1
- latest version

* Fri Nov 02 2012 Caolán McNamara <caolanm@redhat.com> - 0.20120912-2
- add CC-BY-SA to license field

* Wed Sep 12 2012 Caolán McNamara <caolanm@redhat.com> - 0.20120912-1
- latest version

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20120613-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 13 2012 Caolán McNamara <caolanm@redhat.com> - 0.20120613-1
- latest version

* Fri Mar 09 2012 Caolán McNamara <caolanm@redhat.com> - 0.20120309-1
- latest version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20111017-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Caolán McNamara <caolanm@redhat.com> - 0.20111017-1
- latest version

* Mon Aug 08 2011 Caolán McNamara <caolanm@redhat.com> - 0.20110808-1
- latest version

* Thu Jun 09 2011 Caolán McNamara <caolanm@redhat.com> - 0.20110609-1
- latest version

* Fri Mar 18 2011 Caolán McNamara <caolanm@redhat.com> - 0.20110318-1
- latest version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20101221-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Caolán McNamara <caolanm@redhat.com> - 0.20101221-1
- latest version

* Thu Oct 28 2010 Caolán McNamara <caolanm@redhat.com> - 0.20101028-1
- latest version

* Fri Sep 24 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100924-1
- latest version

* Mon Aug 23 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100823-1
- latest version

* Tue Jul 20 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100720-1
- latest version

* Sat Jun 19 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100619-1
- latest version

* Wed May 19 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100519-1
- latest version

* Mon Apr 19 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100419-1
- latest version

* Fri Mar 19 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100319-1
- latest version

* Thu Feb 18 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100218-1
- latest version

* Mon Jan 18 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100118-1
- latest version

* Thu Dec 17 2009 Caolán McNamara <caolanm@redhat.com> - 0.20091217-1
- latest version

* Tue Nov 17 2009 Caolán McNamara <caolanm@redhat.com> - 0.20091117-1
- latest version

* Tue Sep 08 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090908-1
- latest version

* Sat Aug 08 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090808-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090708-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 08 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090708-1
- latest version

* Mon Jun 08 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090608-1
- latest version

* Sun Apr 19 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090419-1
- latest version

* Sun Mar 15 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090315-1
- latest version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090215-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 15 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090215-1
- latest version

* Wed Jan 14 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090114-1
- latest version

* Sat Aug 23 2008 Caolán McNamara <caolanm@redhat.com> - 0.20080823-1
- latest version

* Tue Jul 15 2008 Caolán McNamara <caolanm@redhat.com> - 0.20080715-1
- latest version

* Sat Jun 14 2008 Caolán McNamara <caolanm@redhat.com> - 0.20080614-1
- latest version

* Tue May 13 2008 Caolán McNamara <caolanm@redhat.com> - 0.20080513-1
- latest version

* Mon Apr 07 2008 Caolán McNamara <caolanm@redhat.com> - 0.20080407-1
- latest version

* Tue Mar 04 2008 Caolán McNamara <caolanm@redhat.com> - 0.20080304-1
- source file name changed, update to latest version

* Wed Feb 13 2008 Caolán McNamara <caolanm@redhat.com> - 0.20080213-1
- new version

* Wed Jan 09 2008 Caolán McNamara <caolanm@redhat.com> - 0.20080109-1
- new version

* Sat Dec 08 2007 Caolán McNamara <caolanm@redhat.com> - 0.20071208-1
- new version

* Thu Nov 15 2007 Caolán McNamara <caolanm@redhat.com> - 0.20071114-1
- new version

* Fri Oct 05 2007 Caolán McNamara <caolanm@redhat.com> - 0.20071004-1
- new version

* Mon Sep 03 2007 Caolán McNamara <caolanm@redhat.com> - 0.20070903-1
- new version

* Thu Aug 09 2007 Caolán McNamara <caolanm@redhat.com> - 0.20070803-1
- clarify that is tri-licensed

* Sun Jul 01 2007 Caolán McNamara <caolanm@redhat.com> - 0.20070701-1
- latest version
- near daily updates => move to a pick it up the 1st of the month cycle

* Fri Jun 29 2007 Caolán McNamara <caolanm@redhat.com> - 0.20070629-1
- latest version

* Fri Jun 22 2007 Caolán McNamara <caolanm@redhat.com> - 0.20070622-1
- latest version
