/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/qt6/07_qml_instantiation.yml
 *   Object: QmlAsService
 *   Template: qt6/service_source.j2
 */
#include <QDBusArgument>
#include "QmlAsServiceInterface.hpp"
#include "QmlAsServiceInterfaceAdaptor.hpp"
#include "Connection.hpp"
#include "types.hpp"

using namespace gen::qml_instantiation;
using namespace QmlAsServiceInterfaceUtils;

QmlAsServiceInterface::QmlAsServiceInterface(QObject* parent)
: QObject(parent) {
    registerMetaTypes();
    QObject::connect(
        &Connection::instance(),
        &Connection::connectedChanged,
        this,
        &QmlAsServiceInterface::connectedChanged
    );
    QObject::connect(
        &Connection::instance(),
        &Connection::registrationChanged,
        this,
        &QmlAsServiceInterface::connectedChanged
    );
}

void QmlAsServiceInterface::connect() {
    Connection::instance().registerQmlAsService(this);
}

void QmlAsServiceInterface::disconnect() {
    Connection::instance().unregisterQmlAsService();
}

void QmlAsServiceInterface::finishCall(const QDBusMessage &reply)
{
    Connection::instance().send(reply);
}

bool QmlAsServiceInterface::getConnected() const {
    return (
        Connection::instance().getConnected()
        && Connection::instance().isQmlAsServiceRegistered()
    );
}

PassStructMethodPendingReply::PassStructMethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    m_args = PassStructMethodArgs{
    };
}

PassStructMethodArgs PassStructMethodPendingReply::args() {
    return m_args;
}

void PassStructMethodPendingReply::sendReply(
    QVariant reply
) {
    QmlStruct unmarshalled;
    unmarshalled = reply.value<QmlStruct>();

    sendReply(unmarshalled);
}

void PassStructMethodPendingReply::sendReply(
    const QmlStruct &reply
) {
    auto replyToSend = reply;
    auto dbusReply = m_call.createReply(QVariant::fromValue(replyToSend));
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void PassStructMethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void PassStructMethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void QmlAsServiceInterface::handlePassStructMethodCalled(QDBusMessage call) {
    auto reply = new PassStructMethodPendingReply(call, this);
    emit passStructMethodCalled(reply);
}

void QmlAsServiceInterface::EmitPassStructSignal(
    QmlStruct qmlStruct
) {
    if (Connection::instance().QmlAsService() != nullptr ) {
        emit Connection::instance().QmlAsService()->PassStructSignal(
            qmlStruct
        );
    }
}

void QmlAsServiceInterface::EmitPassStructSignal(
    QVariant qmlStruct
) {
    QmlStruct arg_0;
    arg_0 = qmlStruct.value<QmlStruct>();

    EmitPassStructSignal(
        arg_0
    );
}

PassArrayInArrayMethodPendingReply::PassArrayInArrayMethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    m_args = PassArrayInArrayMethodArgs{
    };
}

PassArrayInArrayMethodArgs PassArrayInArrayMethodPendingReply::args() {
    return m_args;
}

void PassArrayInArrayMethodPendingReply::sendReply(
    QVariant reply
) {
    QList<QList<uint>> unmarshalled;
    for (auto& item_0 : reply.value<QVariantList>()) {
        QList<uint> o_0;
        for (auto& item_1 : item_0.value<QVariantList>()) {
            uint o_1;
            o_1 = item_1.value<uint>();

            o_0.push_back(o_1);
        }

        unmarshalled.push_back(o_0);
    }

    sendReply(unmarshalled);
}

void PassArrayInArrayMethodPendingReply::sendReply(
    const QList<QList<uint>> &reply
) {
    auto replyToSend = reply;
    auto dbusReply = m_call.createReply(QVariant::fromValue(replyToSend));
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void PassArrayInArrayMethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void PassArrayInArrayMethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void QmlAsServiceInterface::handlePassArrayInArrayMethodCalled(QDBusMessage call) {
    auto reply = new PassArrayInArrayMethodPendingReply(call, this);
    emit passArrayInArrayMethodCalled(reply);
}

void QmlAsServiceInterface::EmitPassArrayInArraySignal(
    QList<QList<uint>> listOfLists
) {
    if (Connection::instance().QmlAsService() != nullptr ) {
        emit Connection::instance().QmlAsService()->PassArrayInArraySignal(
            listOfLists
        );
    }
}

void QmlAsServiceInterface::EmitPassArrayInArraySignal(
    QVariant listOfLists
) {
    QList<QList<uint>> arg_0;
    for (auto& item_0 : listOfLists.value<QVariantList>()) {
        QList<uint> o_0;
        for (auto& item_1 : item_0.value<QVariantList>()) {
            uint o_1;
            o_1 = item_1.value<uint>();

            o_0.push_back(o_1);
        }

        arg_0.push_back(o_0);
    }

    EmitPassArrayInArraySignal(
        arg_0
    );
}

PassStructsInArrayMethodPendingReply::PassStructsInArrayMethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    m_args = PassStructsInArrayMethodArgs{
    };
}

PassStructsInArrayMethodArgs PassStructsInArrayMethodPendingReply::args() {
    return m_args;
}

void PassStructsInArrayMethodPendingReply::sendReply(
    QVariant reply
) {
    QList<QmlStruct> unmarshalled;
    for (auto& item_0 : reply.value<QVariantList>()) {
        QmlStruct o_0;
        o_0 = item_0.value<QmlStruct>();

        unmarshalled.push_back(o_0);
    }

    sendReply(unmarshalled);
}

void PassStructsInArrayMethodPendingReply::sendReply(
    const QList<QmlStruct> &reply
) {
    auto replyToSend = reply;
    auto dbusReply = m_call.createReply(QVariant::fromValue(replyToSend));
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void PassStructsInArrayMethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void PassStructsInArrayMethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void QmlAsServiceInterface::handlePassStructsInArrayMethodCalled(QDBusMessage call) {
    auto reply = new PassStructsInArrayMethodPendingReply(call, this);
    emit passStructsInArrayMethodCalled(reply);
}

void QmlAsServiceInterface::EmitPassStructsInArraySignal(
    QList<QmlStruct> listOfStructs
) {
    if (Connection::instance().QmlAsService() != nullptr ) {
        emit Connection::instance().QmlAsService()->PassStructsInArraySignal(
            listOfStructs
        );
    }
}

void QmlAsServiceInterface::EmitPassStructsInArraySignal(
    QVariant listOfStructs
) {
    QList<QmlStruct> arg_0;
    for (auto& item_0 : listOfStructs.value<QVariantList>()) {
        QmlStruct o_0;
        o_0 = item_0.value<QmlStruct>();

        arg_0.push_back(o_0);
    }

    EmitPassStructsInArraySignal(
        arg_0
    );
}

PassDictWithStringsMethodPendingReply::PassDictWithStringsMethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    m_args = PassDictWithStringsMethodArgs{
    };
}

PassDictWithStringsMethodArgs PassDictWithStringsMethodPendingReply::args() {
    return m_args;
}

void PassDictWithStringsMethodPendingReply::sendReply(
    QVariant reply
) {
    QMap<QString, QString> unmarshalled;
    unmarshalled = reply.value<QMap<QString, QString>>();

    sendReply(unmarshalled);
}

void PassDictWithStringsMethodPendingReply::sendReply(
    const QMap<QString, QString> &reply
) {
    auto replyToSend = reply;
    auto dbusReply = m_call.createReply(QVariant::fromValue(replyToSend));
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void PassDictWithStringsMethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void PassDictWithStringsMethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void QmlAsServiceInterface::handlePassDictWithStringsMethodCalled(QDBusMessage call) {
    auto reply = new PassDictWithStringsMethodPendingReply(call, this);
    emit passDictWithStringsMethodCalled(reply);
}

void QmlAsServiceInterface::EmitPassDictWithStringsSignal(
    QMap<QString, QString> dictWithStrings
) {
    if (Connection::instance().QmlAsService() != nullptr ) {
        emit Connection::instance().QmlAsService()->PassDictWithStringsSignal(
            dictWithStrings
        );
    }
}

void QmlAsServiceInterface::EmitPassDictWithStringsSignal(
    QVariant dictWithStrings
) {
    QMap<QString, QString> arg_0;
    arg_0 = dictWithStrings.value<QMap<QString, QString>>();

    EmitPassDictWithStringsSignal(
        arg_0
    );
}

PassDictWithNumbersMethodPendingReply::PassDictWithNumbersMethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    m_args = PassDictWithNumbersMethodArgs{
    };
}

PassDictWithNumbersMethodArgs PassDictWithNumbersMethodPendingReply::args() {
    return m_args;
}

void PassDictWithNumbersMethodPendingReply::sendReply(
    QVariant reply
) {
    QMap<uint, QString> unmarshalled;
    unmarshalled = reply.value<QMap<uint, QString>>();

    sendReply(unmarshalled);
}

void PassDictWithNumbersMethodPendingReply::sendReply(
    const QMap<uint, QString> &reply
) {
    auto replyToSend = reply;
    auto dbusReply = m_call.createReply(QVariant::fromValue(replyToSend));
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void PassDictWithNumbersMethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void PassDictWithNumbersMethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void QmlAsServiceInterface::handlePassDictWithNumbersMethodCalled(QDBusMessage call) {
    auto reply = new PassDictWithNumbersMethodPendingReply(call, this);
    emit passDictWithNumbersMethodCalled(reply);
}

void QmlAsServiceInterface::EmitPassDictWithNumbersSignal(
    QMap<uint, QString> dictWithNumbers
) {
    if (Connection::instance().QmlAsService() != nullptr ) {
        emit Connection::instance().QmlAsService()->PassDictWithNumbersSignal(
            dictWithNumbers
        );
    }
}

void QmlAsServiceInterface::EmitPassDictWithNumbersSignal(
    QVariant dictWithNumbers
) {
    QMap<uint, QString> arg_0;
    arg_0 = dictWithNumbers.value<QMap<uint, QString>>();

    EmitPassDictWithNumbersSignal(
        arg_0
    );
}

PassDictWithStructsMethodPendingReply::PassDictWithStructsMethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    m_args = PassDictWithStructsMethodArgs{
    };
}

PassDictWithStructsMethodArgs PassDictWithStructsMethodPendingReply::args() {
    return m_args;
}

void PassDictWithStructsMethodPendingReply::sendReply(
    QVariant reply
) {
    QMap<QString, QmlStruct> unmarshalled;
    unmarshalled = reply.value<QMap<QString, QmlStruct>>();

    sendReply(unmarshalled);
}

void PassDictWithStructsMethodPendingReply::sendReply(
    const QMap<QString, QmlStruct> &reply
) {
    auto replyToSend = reply;
    auto dbusReply = m_call.createReply(QVariant::fromValue(replyToSend));
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void PassDictWithStructsMethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void PassDictWithStructsMethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void QmlAsServiceInterface::handlePassDictWithStructsMethodCalled(QDBusMessage call) {
    auto reply = new PassDictWithStructsMethodPendingReply(call, this);
    emit passDictWithStructsMethodCalled(reply);
}

void QmlAsServiceInterface::EmitPassDictWithStructsSignal(
    QMap<QString, QmlStruct> dictWithStructs
) {
    if (Connection::instance().QmlAsService() != nullptr ) {
        emit Connection::instance().QmlAsService()->PassDictWithStructsSignal(
            dictWithStructs
        );
    }
}

void QmlAsServiceInterface::EmitPassDictWithStructsSignal(
    QVariant dictWithStructs
) {
    QMap<QString, QmlStruct> arg_0;
    arg_0 = dictWithStructs.value<QMap<QString, QmlStruct>>();

    EmitPassDictWithStructsSignal(
        arg_0
    );
}

PassDictInArrayMethodPendingReply::PassDictInArrayMethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    m_args = PassDictInArrayMethodArgs{
    };
}

PassDictInArrayMethodArgs PassDictInArrayMethodPendingReply::args() {
    return m_args;
}

void PassDictInArrayMethodPendingReply::sendReply(
    QVariant reply
) {
    QList<QMap<QString, QString>> unmarshalled;
    for (auto& item_0 : reply.value<QVariantList>()) {
        QMap<QString, QString> o_0;
        o_0 = item_0.value<QMap<QString, QString>>();

        unmarshalled.push_back(o_0);
    }

    sendReply(unmarshalled);
}

void PassDictInArrayMethodPendingReply::sendReply(
    const QList<QMap<QString, QString>> &reply
) {
    auto replyToSend = reply;
    auto dbusReply = m_call.createReply(QVariant::fromValue(replyToSend));
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void PassDictInArrayMethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void PassDictInArrayMethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void QmlAsServiceInterface::handlePassDictInArrayMethodCalled(QDBusMessage call) {
    auto reply = new PassDictInArrayMethodPendingReply(call, this);
    emit passDictInArrayMethodCalled(reply);
}

void QmlAsServiceInterface::EmitPassDictInArraySignal(
    QList<QMap<QString, QString>> listOfDicts
) {
    if (Connection::instance().QmlAsService() != nullptr ) {
        emit Connection::instance().QmlAsService()->PassDictInArraySignal(
            listOfDicts
        );
    }
}

void QmlAsServiceInterface::EmitPassDictInArraySignal(
    QVariant listOfDicts
) {
    QList<QMap<QString, QString>> arg_0;
    for (auto& item_0 : listOfDicts.value<QVariantList>()) {
        QMap<QString, QString> o_0;
        o_0 = item_0.value<QMap<QString, QString>>();

        arg_0.push_back(o_0);
    }

    EmitPassDictInArraySignal(
        arg_0
    );
}

PassDictInDictMethodPendingReply::PassDictInDictMethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    m_args = PassDictInDictMethodArgs{
    };
}

PassDictInDictMethodArgs PassDictInDictMethodPendingReply::args() {
    return m_args;
}

void PassDictInDictMethodPendingReply::sendReply(
    QVariant reply
) {
    QMap<QString, QMap<QString, QString>> unmarshalled;
    unmarshalled = reply.value<QMap<QString, QMap<QString, QString>>>();

    sendReply(unmarshalled);
}

void PassDictInDictMethodPendingReply::sendReply(
    const QMap<QString, QMap<QString, QString>> &reply
) {
    auto replyToSend = reply;
    auto dbusReply = m_call.createReply(QVariant::fromValue(replyToSend));
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void PassDictInDictMethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void PassDictInDictMethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void QmlAsServiceInterface::handlePassDictInDictMethodCalled(QDBusMessage call) {
    auto reply = new PassDictInDictMethodPendingReply(call, this);
    emit passDictInDictMethodCalled(reply);
}

void QmlAsServiceInterface::EmitPassDictInDictSignal(
    QMap<QString, QMap<QString, QString>> dictOfDicts
) {
    if (Connection::instance().QmlAsService() != nullptr ) {
        emit Connection::instance().QmlAsService()->PassDictInDictSignal(
            dictOfDicts
        );
    }
}

void QmlAsServiceInterface::EmitPassDictInDictSignal(
    QVariant dictOfDicts
) {
    QMap<QString, QMap<QString, QString>> arg_0;
    arg_0 = dictOfDicts.value<QMap<QString, QMap<QString, QString>>>();

    EmitPassDictInDictSignal(
        arg_0
    );
}

PassArrayInDictMethodPendingReply::PassArrayInDictMethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    m_args = PassArrayInDictMethodArgs{
    };
}

PassArrayInDictMethodArgs PassArrayInDictMethodPendingReply::args() {
    return m_args;
}

void PassArrayInDictMethodPendingReply::sendReply(
    QVariant reply
) {
    QMap<QString, QList<QString>> unmarshalled;
    unmarshalled = reply.value<QMap<QString, QList<QString>>>();

    sendReply(unmarshalled);
}

void PassArrayInDictMethodPendingReply::sendReply(
    const QMap<QString, QList<QString>> &reply
) {
    auto replyToSend = reply;
    auto dbusReply = m_call.createReply(QVariant::fromValue(replyToSend));
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void PassArrayInDictMethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void PassArrayInDictMethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void QmlAsServiceInterface::handlePassArrayInDictMethodCalled(QDBusMessage call) {
    auto reply = new PassArrayInDictMethodPendingReply(call, this);
    emit passArrayInDictMethodCalled(reply);
}

void QmlAsServiceInterface::EmitPassArrayInDictSignal(
    QMap<QString, QList<QString>> dictOfLists
) {
    if (Connection::instance().QmlAsService() != nullptr ) {
        emit Connection::instance().QmlAsService()->PassArrayInDictSignal(
            dictOfLists
        );
    }
}

void QmlAsServiceInterface::EmitPassArrayInDictSignal(
    QVariant dictOfLists
) {
    QMap<QString, QList<QString>> arg_0;
    arg_0 = dictOfLists.value<QMap<QString, QList<QString>>>();

    EmitPassArrayInDictSignal(
        arg_0
    );
}

PassDictInArrayInDictMethodPendingReply::PassDictInArrayInDictMethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    m_args = PassDictInArrayInDictMethodArgs{
    };
}

PassDictInArrayInDictMethodArgs PassDictInArrayInDictMethodPendingReply::args() {
    return m_args;
}

void PassDictInArrayInDictMethodPendingReply::sendReply(
    QVariant reply
) {
    QMap<QString, QList<QMap<QString, QString>>> unmarshalled;
    unmarshalled = reply.value<QMap<QString, QList<QMap<QString, QString>>>>();

    sendReply(unmarshalled);
}

void PassDictInArrayInDictMethodPendingReply::sendReply(
    const QMap<QString, QList<QMap<QString, QString>>> &reply
) {
    auto replyToSend = reply;
    auto dbusReply = m_call.createReply(QVariant::fromValue(replyToSend));
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void PassDictInArrayInDictMethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void PassDictInArrayInDictMethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void QmlAsServiceInterface::handlePassDictInArrayInDictMethodCalled(QDBusMessage call) {
    auto reply = new PassDictInArrayInDictMethodPendingReply(call, this);
    emit passDictInArrayInDictMethodCalled(reply);
}

void QmlAsServiceInterface::EmitPassDictInArrayInDictSignal(
    QMap<QString, QList<QMap<QString, QString>>> dictOfListsOfDicts
) {
    if (Connection::instance().QmlAsService() != nullptr ) {
        emit Connection::instance().QmlAsService()->PassDictInArrayInDictSignal(
            dictOfListsOfDicts
        );
    }
}

void QmlAsServiceInterface::EmitPassDictInArrayInDictSignal(
    QVariant dictOfListsOfDicts
) {
    QMap<QString, QList<QMap<QString, QString>>> arg_0;
    arg_0 = dictOfListsOfDicts.value<QMap<QString, QList<QMap<QString, QString>>>>();

    EmitPassDictInArrayInDictSignal(
        arg_0
    );
}

PassDictInArrayInArrayMethodPendingReply::PassDictInArrayInArrayMethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    m_args = PassDictInArrayInArrayMethodArgs{
    };
}

PassDictInArrayInArrayMethodArgs PassDictInArrayInArrayMethodPendingReply::args() {
    return m_args;
}

void PassDictInArrayInArrayMethodPendingReply::sendReply(
    QVariant reply
) {
    QList<QList<QMap<QString, QString>>> unmarshalled;
    for (auto& item_0 : reply.value<QVariantList>()) {
        QList<QMap<QString, QString>> o_0;
        for (auto& item_1 : item_0.value<QVariantList>()) {
            QMap<QString, QString> o_1;
            o_1 = item_1.value<QMap<QString, QString>>();

            o_0.push_back(o_1);
        }

        unmarshalled.push_back(o_0);
    }

    sendReply(unmarshalled);
}

void PassDictInArrayInArrayMethodPendingReply::sendReply(
    const QList<QList<QMap<QString, QString>>> &reply
) {
    auto replyToSend = reply;
    auto dbusReply = m_call.createReply(QVariant::fromValue(replyToSend));
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void PassDictInArrayInArrayMethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void PassDictInArrayInArrayMethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void QmlAsServiceInterface::handlePassDictInArrayInArrayMethodCalled(QDBusMessage call) {
    auto reply = new PassDictInArrayInArrayMethodPendingReply(call, this);
    emit passDictInArrayInArrayMethodCalled(reply);
}

void QmlAsServiceInterface::EmitPassDictInArrayInArraySignal(
    QList<QList<QMap<QString, QString>>> listOfListsOfDicts
) {
    if (Connection::instance().QmlAsService() != nullptr ) {
        emit Connection::instance().QmlAsService()->PassDictInArrayInArraySignal(
            listOfListsOfDicts
        );
    }
}

void QmlAsServiceInterface::EmitPassDictInArrayInArraySignal(
    QVariant listOfListsOfDicts
) {
    QList<QList<QMap<QString, QString>>> arg_0;
    for (auto& item_0 : listOfListsOfDicts.value<QVariantList>()) {
        QList<QMap<QString, QString>> o_0;
        for (auto& item_1 : item_0.value<QVariantList>()) {
            QMap<QString, QString> o_1;
            o_1 = item_1.value<QMap<QString, QString>>();

            o_0.push_back(o_1);
        }

        arg_0.push_back(o_0);
    }

    EmitPassDictInArrayInArraySignal(
        arg_0
    );
}

PassDictWithEnumsMethodPendingReply::PassDictWithEnumsMethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    m_args = PassDictWithEnumsMethodArgs{
    };
}

PassDictWithEnumsMethodArgs PassDictWithEnumsMethodPendingReply::args() {
    return m_args;
}

void PassDictWithEnumsMethodPendingReply::sendReply(
    QVariant reply
) {
    QMap<QmlEnum::Type, QmlEnum::Type> unmarshalled;
    unmarshalled = reply.value<QMap<QmlEnum::Type, QmlEnum::Type>>();

    sendReply(unmarshalled);
}

void PassDictWithEnumsMethodPendingReply::sendReply(
    const QMap<QmlEnum::Type, QmlEnum::Type> &reply
) {
    auto replyToSend = *reinterpret_cast<const QMap<int, int>*>(&reply);
    auto dbusReply = m_call.createReply(QVariant::fromValue(replyToSend));
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void PassDictWithEnumsMethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void PassDictWithEnumsMethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<QmlAsServiceInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void QmlAsServiceInterface::handlePassDictWithEnumsMethodCalled(QDBusMessage call) {
    auto reply = new PassDictWithEnumsMethodPendingReply(call, this);
    emit passDictWithEnumsMethodCalled(reply);
}

void QmlAsServiceInterface::EmitPassDictWithEnumsSignal(
    QMap<QmlEnum::Type, QmlEnum::Type> dictOfEnumsToEnums
) {
    if (Connection::instance().QmlAsService() != nullptr ) {
        emit Connection::instance().QmlAsService()->PassDictWithEnumsSignal(
            *reinterpret_cast<const QMap<int, int>*>(&dictOfEnumsToEnums)
        );
    }
}

void QmlAsServiceInterface::EmitPassDictWithEnumsSignal(
    QVariant dictOfEnumsToEnums
) {
    QMap<QmlEnum::Type, QmlEnum::Type> arg_0;
    arg_0 = dictOfEnumsToEnums.value<QMap<QmlEnum::Type, QmlEnum::Type>>();

    EmitPassDictWithEnumsSignal(
        arg_0
    );
}


void QmlAsServiceInterface::emitPropertiesChangedSignal(const QVariantMap &changedProps) {
    auto signal = QDBusMessage::createSignal(
        "/com/yarpc/testservice/qmlInstantiation",
        "org.freedesktop.DBus.Properties",
        "PropertiesChanged"
    );
    signal << "com.yarpc.testservice.qmlInstantiation";
    signal << changedProps;
    signal << QStringList{};
    Connection::instance().send(signal);
}