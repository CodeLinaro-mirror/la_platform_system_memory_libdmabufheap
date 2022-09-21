Name: libdmabufheap
Version: 1.0
Release: r0
Summary:  libdmabufheap rpm package

License: Apache-2.0

Group: base
URL: https://www.codelinaro.org/
#Source0: libdmabufheap-1.0.tar.gz
Source0: %{name}-%{version}.tar.gz

BuildRequires: autoconf automake libtool gcc-g++ libbase-dev libcutils-dev

%description
libdmabufheap supports allocation in DMA-BUF heaps and ION heaps

%package -n libdmabufheap-dev
Summary: libdmabufheap-1.0 - Development files
License: Apache-2.0
Group: devel
Requires: %{name} = %{version}-%{release}

%description -n libdmabufheap-dev
libdmabufheap supports allocation in DMA-BUF heaps and ION heap.
This package contains symbolic links,header files, and related
items necessary for software development.

%prep
%autosetup -n libdmabufheap

%build
autoreconf -if
%configure --with-libdmabufheap-includes=%{_builddir}/include/BufferAllocator

%make_build

%install
%make_install

%check

%files
%doc
%{_libdir}/libdmabufheap.a
%{_libdir}/libdmabufheap.la
%{_libdir}/libdmabufheap.so.0.0.0
%{_libdir}/libdmabufheap.so.0

%files -n libdmabufheap-dev
%defattr(-,-,-,-)
%{_libdir}/libdmabufheap.so
%{_libdir}/pkgconfig/libdmabufheap.pc
%{_includedir}/BufferAllocator/BufferAllocator.h
%{_includedir}/BufferAllocator/BufferAllocatorWrapper.h
%{_includedir}/BufferAllocator/dmabufheap-defs.h
