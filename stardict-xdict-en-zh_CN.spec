%define	version	2.4.2
%define release %mkrel 9
%define dict_format_version	2.4.2

Summary:	Simplified Chinese dictionary for stardict 2
Name:		stardict-xdict-en-zh_CN
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Databases
URL:		http://stardict.sourceforge.net/
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
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/stardict/dic
install -m 0644 * %{buildroot}%{_datadir}/stardict/dic

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/stardict/dic/*


