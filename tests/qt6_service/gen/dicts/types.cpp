/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/qt6/05_dicts.yml
 *   Template: qt6/types_source.j2
 */
#include "types.hpp"
#include <QList>
#include <QDBusMetaType>

void gen::dicts::registerMetaTypes() {
    qRegisterMetaType<StructDict>("StructDict");
    qDBusRegisterMetaType<StructDict>();
    qRegisterMetaType<SimonsDict>("SimonsDict");
    qDBusRegisterMetaType<SimonsDict>();
    qRegisterMetaType<QList<QMap<QString, uint>>>("QList<QMap<QString, uint>>");
    qDBusRegisterMetaType<QList<QMap<QString, uint>>>();
    qRegisterMetaType<QMap<bool, QString>>("QMap<bool, QString>");
    qDBusRegisterMetaType<QMap<bool, QString>>();
    qRegisterMetaType<QMap<QString, QMap<QString, uint>>>("QMap<QString, QMap<QString, uint>>");
    qDBusRegisterMetaType<QMap<QString, QMap<QString, uint>>>();
    qRegisterMetaType<QMap<QString, SimonsDict>>("QMap<QString, SimonsDict>");
    qDBusRegisterMetaType<QMap<QString, SimonsDict>>();
    qRegisterMetaType<QMap<QString, QString>>("QMap<QString, QString>");
    qDBusRegisterMetaType<QMap<QString, QString>>();
    qRegisterMetaType<QMap<int, QString>>("QMap<int, QString>");
    qDBusRegisterMetaType<QMap<int, QString>>();
    qRegisterMetaType<QMap<ushort, QString>>("QMap<ushort, QString>");
    qDBusRegisterMetaType<QMap<ushort, QString>>();
    qRegisterMetaType<QMap<QString, StructDict>>("QMap<QString, StructDict>");
    qDBusRegisterMetaType<QMap<QString, StructDict>>();
    qRegisterMetaType<QMap<short, QString>>("QMap<short, QString>");
    qDBusRegisterMetaType<QMap<short, QString>>();
    qRegisterMetaType<QMap<QString, uint>>("QMap<QString, uint>");
    qDBusRegisterMetaType<QMap<QString, uint>>();
    qRegisterMetaType<QMap<QString, QString>>("QMap<QString, QString>");
    qDBusRegisterMetaType<QMap<QString, QString>>();
    qRegisterMetaType<QMap<double, QString>>("QMap<double, QString>");
    qDBusRegisterMetaType<QMap<double, QString>>();
    qRegisterMetaType<QMap<QString, StructDict>>("QMap<QString, StructDict>");
    qDBusRegisterMetaType<QMap<QString, StructDict>>();
    qRegisterMetaType<QMap<uchar, QString>>("QMap<uchar, QString>");
    qDBusRegisterMetaType<QMap<uchar, QString>>();
    qRegisterMetaType<QMap<QString, QList<QMap<QString, uint>>>>("QMap<QString, QList<QMap<QString, uint>>>");
    qDBusRegisterMetaType<QMap<QString, QList<QMap<QString, uint>>>>();
    qRegisterMetaType<QMap<qlonglong, QString>>("QMap<qlonglong, QString>");
    qDBusRegisterMetaType<QMap<qlonglong, QString>>();
    qRegisterMetaType<QMap<QString, uint>>("QMap<QString, uint>");
    qDBusRegisterMetaType<QMap<QString, uint>>();
    qRegisterMetaType<QMap<qulonglong, QString>>("QMap<qulonglong, QString>");
    qDBusRegisterMetaType<QMap<qulonglong, QString>>();
    qRegisterMetaType<QMap<uint, QString>>("QMap<uint, QString>");
    qDBusRegisterMetaType<QMap<uint, QString>>();
}

bool gen::dicts::operator!=(const QMap<QString, StructDict> &lhs, const QMap<QString, StructDict> &rhs) {
    if (lhs.size() != rhs.size()) {
        return true;
    }
    for (auto i=lhs.keyBegin(); i!=lhs.keyEnd(); ++i) {
        if (!rhs.contains(*i))
        {
            return true;
        }
        if (lhs[*i] != rhs[*i]) {
            return true;
        }
    }
    return false;
}

bool gen::dicts::operator!=(const QMap<QString, SimonsDict> &lhs, const QMap<QString, SimonsDict> &rhs) {
    if (lhs.size() != rhs.size()) {
        return true;
    }
    for (auto i=lhs.keyBegin(); i!=lhs.keyEnd(); ++i) {
        if (!rhs.contains(*i))
        {
            return true;
        }
        if (lhs[*i] != rhs[*i]) {
            return true;
        }
    }
    return false;
}
