###################################################################################
#	Marvell GPL License
#	
#	If you received this File from Marvell, you may opt to use, redistribute and/or
#	modify this File in accordance with the terms and conditions of the General
#	Public License Version 2, June 1991 (the "GPL License"), a copy of which is
#	available along with the File in the license.txt file or by writing to the Free
#	Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 or
#	on the worldwide web at http://www.gnu.org/licenses/gpl.txt.
#	
#	THE FILE IS DISTRIBUTED AS-IS, WITHOUT WARRANTY OF ANY KIND, AND THE IMPLIED
#	WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE ARE EXPRESSLY
#	DISCLAIMED.  The GPL License provides additional details about this warranty
#	disclaimer.
###################################################################################

class DUTGeneralInfo(object):
    def __init__(self):
        self.device_name = []
        self.dut_corner = []
        self.lot_number = []
        self.xml_file = []


class Portdata(object):
    def __init__(self):
        self.port_number = []
        self.destination_port = []
        self.port_mode = []
        self.port_speed = []
        self.port_clock_source = []
        self.port_ppm = []
        self.port_training = []
        self.adaptive_serdes_tune = []
        self.port_fec = []
        self.tx_amp = []
        self.tx_emph_0 = []
        self.tx_emph_1 = []
        self.pve_source = []
        self.pve_destination = []
        self.start_serdes = []
        self.stop_serdes = []
        self.port_interconnect = []


