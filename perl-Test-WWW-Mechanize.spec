%define upstream_name	 Test-WWW-Mechanize
%define upstream_version 1.44

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Testing-specific WWW::Mechanize subclass
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/Test-WWW-Mechanize-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp::Assert::More)
BuildRequires:	perl(CGI)
BuildRequires:	perl(HTML::Lint)
BuildRequires:	perl(HTTP::Server::Simple)
BuildRequires:	perl(HTML::TreeBuilder)
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl(Test::LongString)
BuildRequires:	perl(URI)
BuildRequires:	perl(WWW::Mechanize) 

BuildArch:	noarch

%description
Test::WWW::Mechanize is a subclass of WWW::Mechanize that incorporates features
for web application testing.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# change listening port
perl -pi -e 's/13432/17987/' t/TestServer.pm
%make test

%install
%makeinstall_std

%files
%doc Changes 
%{perl_vendorlib}/Test
%{_mandir}/man3/*

%changelog
* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.340.0-1mdv2011
+ Revision: 690330
- update to new version 1.34

* Sat May 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.320.0-1
+ Revision: 674606
- update to new version 1.32

* Wed Jul 14 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.300.0-1mdv2011.0
+ Revision: 553058
- change listening port of test server
- adding missing buildrequires:
- update to 1.30

* Sun Apr 18 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.280.0-1mdv2010.1
+ Revision: 536216
- update to 1.28

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.240.0-1mdv2010.0
+ Revision: 406188
- rebuild using %%perl_convert_version

* Sun Jan 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.24-1mdv2009.1
+ Revision: 330915
- update to new version 1.24

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.20-2mdv2009.0
+ Revision: 268764
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-1mdv2009.0
+ Revision: 194954
- update to new version 1.20

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Dec 07 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.18-1mdv2008.1
+ Revision: 116171
- update to new version 1.18

* Sat Nov 17 2007 Funda Wang <fwang@mandriva.org> 1.16-2mdv2008.1
+ Revision: 109357
- rebuild

* Fri Nov 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.16-1mdv2008.1
+ Revision: 105438
- new version

* Mon May 21 2007 Michael Scherer <misc@mandriva.org> 1.14-1mdv2008.0
+ Revision: 29046
- Update to new version 1.14


* Sat Jul 08 2006 Michael Scherer <misc@mandriva.org> 1.12-1mdv2007.0
- New release 1.12

* Wed Jun 21 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-1mdv2007.0
- New version 1.10
- spec cleanup

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.08-4mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL

* Tue Dec 27 2005 Michael Scherer <misc@mandriva.org> 1.08-3mdk
- Do not ship empty dir

* Fri Dec 16 2005 Michael Scherer <misc@mandriva.org> 1.08-2mdk
- fix BuildRequires

* Wed Dec 07 2005 Michael Scherer <misc@mandriva.org> 1.08-1mdk
- New release 1.08

* Sat Nov 05 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.06-4mdk
- Fix BuildRequires

* Fri Nov 04 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.06-3mdk
- Fix BuildRequires

* Fri Nov 04 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.06-2mdk
- Fix BuildRequires

* Sat Oct 01 2005 Michael Scherer <misc@mandriva.org> 1.06-1mdk
- First mandriva package


