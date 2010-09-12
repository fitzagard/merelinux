Summary: Smart Package Manager
Name: smart
Version: 1.4
Release: 2
Group: System Environment/Base
License: GPLv2
Distribution: LightCube OS
Vendor: LightCube Solutions
URL: http://labix.org/smart
Source0: http://dev.lightcube.us/sources/%{name}/%{name}-%{version}-r993.tar.bz2

Requires: pyliblzma, rpm-python
BuildRequires: digest(sha1:%{SOURCE0}) = d92d95515be781a024dede22ae6ee028418c4f62
BuildRequires: Python-devel
BuildRequires: gettext

%description
The Smart Package Manager project has the ambitious objective of creating smart
and portable algorithms for solving adequately the problem of managing software
upgrades and installation. This tool works in all major distributions and will
bring notable advantages over native tools currently in use (APT, APT-RPM, YUM,
URPMI, etc).

%prep
%setup -q -n %{name}-%{version}-r993

%build
make

%install
make DESTDIR=%{buildroot} install
find %{buildroot}/usr/share/man -type f -exec bzip2 -9 '{}' \;
install -dv %{buildroot}/usr/lib/smart
cat > %{buildroot}/usr/lib/smart/distro.py << "EOF"
if not sysconf.getReadOnly():
            sysconf.set("channels.lightcube", {
                            "type": "rpm-md",
                            "name": "LightCube OS Repository",
                            "baseurl": "http://dev.lightcube.us/repos"
                        })
EOF
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
/usr/bin/smart
/usr/lib/python2.7/site-packages/*
/usr/lib/smart
/usr/share/man/man8/smart.8.bz2

%changelog
* Sun Sep 05 2010 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> - 1.4-2
- Add configuration for LightCube OS repository

* Wed Sep 01 2010 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> - 1.4-1
- Initial version