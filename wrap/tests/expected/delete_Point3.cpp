// automatically generated by wrap
#include <wrap/matlab.h>
#include <Point3.h>
using namespace geometry;
void mexFunction(int nargout, mxArray *out[], int nargin, const mxArray *in[])
{
  checkArguments("delete_Point3",nargout,nargin,1);
  delete_shared_ptr< Point3 >(in[0],"Point3");
}
