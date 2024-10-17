%define	version	2.4.2
%define release 21
%define dict_format_version	2.4.2

Summary:	Simplified Chinese dictionary for stardict 2
Name:		stardict-xdict-en-zh_CN
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Databases
URL:		https://stardict.sourceforge.net/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch

Source0:	ftp://osdn.dl.sourceforge.net/pub/sourceforge/s/st/stardict/stardict-xdict-ec-gb-%{version}.tar.bz2

Provides:	stardict-dictionary = %{dict_format_version}
Requires:	stardict >= %{dict_format_version}

%description
Xdict is an old English to Chinese dictionary application.
This package contains xdict database converted into stardict format.

%prep
%setup -q -n stardict-xdict-ec-gb-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/stardict/dic
install -m 0644 * $RPM_BUILD_ROOT%{_datadir}/stardict/dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/stardict/dic/*




%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 2.4.2-9mdv2011.0
+ Revision: 670198
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.4.2-8mdv2011.0
+ Revision: 607748
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.4.2-7mdv2010.1
+ Revision: 521681
- rebuilt for 2010.1

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.4.2-6mdv2009.0
+ Revision: 225476
- rebuild

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 2.4.2-5mdv2008.1
+ Revision: 168509
- rebuild
- fix summary
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Thu Mar 08 2007 Oden Eriksson <oeriksson@mandriva.com> 2.4.2-4mdv2007.1
+ Revision: 137970
- Import stardict-xdict-en-zh_CN

* Thu Mar 08 2007 Oden Eriksson <oeriksson@mandriva.com> 2.4.2-4mdv2007.1
- use the %%mkrel macro

* Sun Oct 02 2005 Abel Cheung <deaddog@mandriva.org> 2.4.2-3mdk
- Rebuild

* Wed Jun 02 2004 Abel Cheung <deaddog@deaddog.org> 2.4.2-2mdk
- Dictionaries require main program as well

