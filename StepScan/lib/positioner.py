"""
Positioner for Step Scan
"""

from epics import PV, caget

class Positioner(object):
    """a positioner for a scan
This **ONLY** sets an ordinate value for scan, it does *NOT*
do a readback on this position -- add a ScanDetector for that!
    """
    def __init__(self, pvname, label=None, array=None, **kws):
        self.pv = PV(pvname)
        self.pv.get()
        self.pv.get_ctrlvars()

        self.label = label
        if label is None:
            desc = pvname
            if '.' in pvname:
                idot = pvname.index('.')
                descpv = pvname[:idot] + '.DESC'
            else:
                descpv = pvname + '.DESC'                
            try:
                desc = caget(descpv)
            except:
                pass
            self.label = desc
                        
        self.array = array
        self.extra_pvs = []

    def __repr__(self):
        out = "<Positioner '%s': %i points" % (self.pv.pvname, len(self.array))
        if len(self.array) > 0:
            amin = '%g' % (min(self.array))
            amax = '%g' % (max(self.array))
            out = "%s, range: [%s, %s]" % (out, amin, amax)
        return "%s>" % out

    def __onComplete(self, pvname=None, **kws):
        self.done = True

    def set_array(self, start=None, stop=None, step=None, npts=None):
        """set positioner array with start/stop/step/npts"""
        print 'hello set array'

    def move_to_start(self, wait=False):
        """ move to starting position"""
        return self.move_to_pos(0, wait=wait)

    def current(self):
        "return current position"
        return self.pv.get()

    def verify_array(self):
        """return True if array is within the """
        array = self.array
        if array is None:
            return True
        if self.pv.upper_ctrl_limit == self.pv.lower_ctrl_limit:
            return True
        if ((self.pv.upper_ctrl_limit is not None and
             self.pv.upper_ctrl_limit < max(array)) or
            (self.pv.lower_ctrl_limit is not None and
             self.pv.lower_ctrl_limit > min(array))):
            return False
        return True

    def move_to(self, value, wait=False, timeout=600):
        """move to a value, optionally waiting"""
        self.pv.put(value, wait=wait, timeout=timeout)
        

    def move_to_pos(self, i, wait=False, timeout=600):
        """move to i-th position in positioner array"""
        if self.array is None or not self.pv.connected:
            return
        self.done = False
        self.pv.put(self.array[i], callback=self.__onComplete)
        if wait:
            t0 = time.time()
            while not self.done and time.time()-t0 < timeout:
                time.sleep(1.e-4)

    def pre_scan(self):
        "method to run prior to scan: override for real action"
        pass

    def post_scan(self):
        "method to run after to scan: override for real action"
        pass

    def at_break(self, breakpoint=None):
        "method to run at break points: override for real action"
        pass

